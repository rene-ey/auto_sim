from evaluate_simulations import evaluate_simulations, find_optimal_durations

# Anzahl der Simulationsdurchläufe und Konfigurationsdatei
num_simulations = 5
simulation_config = 'simulation_v1.sumocfg'
xml_file = 'trafficlight.add.xml'

evaluation_results = evaluate_simulations(simulation_config, num_simulations, xml_file)

for index, result in enumerate(evaluation_results, start=1):
    num_simulations, new_duration_phase1, new_duration_phase3, total_waiting_time = result
    print(f"Simulation {index}: Anzahl der Durchläufe: {num_simulations}, Neue Dauer Phase 1: {new_duration_phase1}, Neue Dauer Phase 3: {new_duration_phase3}, Gesamtwartezeit: {total_waiting_time}")


# Finden der optimalen Dauern für die Ampelphasen
phase1_range = range(10, 60, 20)  # Variiert von 10 bis 90 Sekunden in 10er-Schritten
phase3_range = range(10, 60, 20)  # Variiert von 10 bis 90 Sekunden in 10er-Schritten
best_durations, best_waiting_time = find_optimal_durations(simulation_config, xml_file, phase1_range, phase3_range)

print(f"Optimale Dauern - Phase 1: {best_durations[0]} s, Phase 3: {best_durations[1]} s, Beste Wartezeit: {best_waiting_time}")
