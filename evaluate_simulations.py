from xml_handler import load_xml_file, update_phase_durations, save_xml_file, extract_car_numbers
from simulation_handler import run_simulation
import csv
import os


def calculate_waiting_time(xml_file):
    try:
        tree, root = load_xml_file(xml_file)
        if tree is not None and root is not None:
            sum_waiting_time = 0
            for tripinfo in root.findall(".//tripinfo"):
                waiting_time = float(tripinfo.get("waitingTime"))
                sum_waiting_time += waiting_time
            return sum_waiting_time
    except Exception as e:
        print("Fehler beim Verarbeiten der XML-Datei:", str(e))
    return None

def evaluate_simulations(simulation_config, num_simulations, xml_file):
    results = []

    for _ in range(num_simulations):
        # Aktualisiere die Ampelzeiten in der XML-Datei für diesen Durchlauf
        if _ == 1:
          new_duration_phase1 = 42
          new_duration_phase3 = 42
        elif _ == 2:
          new_duration_phase1 = 12
          new_duration_phase3 = 12
        elif _ == 3:
          new_duration_phase1 = 20
          new_duration_phase3 = 20
        elif _ == 4:
          new_duration_phase1 = 30
          new_duration_phase3 = 35
        else:
          new_duration_phase1 = 42
          new_duration_phase3 = 12
        tree, root = load_xml_file(xml_file)
        if tree is not None and root is not None:
            update_phase_durations(root, new_duration_phase1, new_duration_phase3)
            save_xml_file(tree, xml_file)

        # Führe die Simulation für diesen Durchlauf aus
        run_simulation(simulation_config)

        # Berechne die Wartezeit und speichere sie in den Ergebnissen
        total_waiting_time = calculate_waiting_time('Outputs/tripinfo_v1.xml')  # Ersetze durch den tatsächlichen Dateinamen
        if total_waiting_time is not None:
            results.append((num_simulations, new_duration_phase1, new_duration_phase3, total_waiting_time))

    return results


def find_optimal_durations(simulation_config, xml_file, phase1_range, phase3_range):
  best_waiting_time = float('inf')
  best_durations = (0, 0)


  file_exists = os.path.isfile("results.csv")

  # CSV-Datei für die Speicherung der Ergebnisse vorbereiten
  with open("results.csv", "a", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # CSV-Header schreiben, wenn die Datei noch nicht existiert
    if not file_exists:
      csv_writer.writerow(["car_numbers1", "car_numbers2", "car_numbers3", "car_numbers4", "duration1", "duration3",
                           "total_waiting_time"])

    car_numbers = extract_car_numbers()
    for duration1 in phase1_range:
      for duration3 in phase3_range:
        tree, root = load_xml_file(xml_file)
        if tree is not None and root is not None:
          update_phase_durations(root, duration1, duration3)
          save_xml_file(tree, xml_file)

        run_simulation(simulation_config)
        total_waiting_time = calculate_waiting_time('Outputs/tripinfo_v1.xml')

        if total_waiting_time < best_waiting_time:
          best_waiting_time = total_waiting_time
          best_durations = (duration1, duration3)

        # Ergebnisse in die CSV-Datei schreiben
        csv_writer.writerow([
          car_numbers.get("car_flow", 0),
          car_numbers.get("car_flow1", 0),
          car_numbers.get("car_flow2", 0),
          car_numbers.get("car_flow3", 0),
          duration1,
          duration3,
          total_waiting_time
        ])

  return best_durations, best_waiting_time
