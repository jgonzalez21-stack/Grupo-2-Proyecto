import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <makespan>")
        return

    makespan = sys.argv[1]
    print("Makespan objetivo:", makespan)

if __name__ == "__main__":
    main()

Print(maskepan)