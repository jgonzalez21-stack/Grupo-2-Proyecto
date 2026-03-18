import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <makespan>")
        return

    makespan = sys.argv[1]
    print("Makespan objetivo:", makespan)

if __name__ == "__main__":
    main()


def leer_tareas():
    with open("tareas.txt") as f:
        return [line.strip().split(",") for line in f]

def leer_recursos():
    with open("recursos.txt") as f:
        return [line.strip().split(",") for line in f]
    