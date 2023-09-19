import xml.etree.ElementTree as ET

def load_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        return tree, tree.getroot()
    except Exception as e:
        print("Fehler beim Laden der XML-Datei:", str(e))
        return None, None

def update_phase_durations(root, new_duration_phase1, new_duration_phase3):
    try:
        tl_logic_element = root.find(".//tlLogic[@id='J1']")
        for phase in tl_logic_element.findall(".//phase"):
            state = phase.get("state")
            if state == "rrrGGGgrrrGGGrrrrrrrr":
                phase.set("duration", str(new_duration_phase1))
            elif state == "GGgrrrrGGgrrrrrrrrrrr":
                phase.set("duration", str(new_duration_phase3))
    except Exception as e:
        print("Fehler beim Aktualisieren der Phasen-Dauern:", str(e))

def save_xml_file(tree, file_path):
    try:
        tree.write(file_path)
        print("XML-Datei erfolgreich gespeichert.")
    except Exception as e:
        print("Fehler beim Speichern der XML-Datei:", str(e))


def extract_car_numbers():
  file_path = 'simulation_demand_v1.rou.xml'
  car_numbers = {}

  try:
    tree, root = load_xml_file(file_path)

    if root is not None:
      for flow in root.findall(".//flow"):
        flow_id = flow.get("id")
        number = int(flow.get("number"))
        car_numbers[flow_id] = number

      return car_numbers
    else:
      print("Die XML-Root konnte nicht geladen werden.")
      return None

  except Exception as e:
    print("Fehler beim Extrahieren der Autonummern:", str(e))
    return None
