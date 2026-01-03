import sys

def ft_command_quest():
    i = 1
    print("=== Command Quest ===")

    if (len(sys.argv) == 1):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")

    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv)-1}")

        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

        print(f"Total arguments: {len(sys.argv)}")
    
ft_command_quest()