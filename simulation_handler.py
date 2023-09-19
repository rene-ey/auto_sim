import subprocess

def run_simulation(simulation_config):
    try:
        command = f"sumo -c {simulation_config}"
        result = subprocess.run(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("Simulation erfolgreich beendet.")
        else:
            print("Fehler bei der Ausführung der Simulation:")
            print(result.stderr)
    except Exception as e:
        print("Fehler bei der Ausführung der Simulation:", str(e))
