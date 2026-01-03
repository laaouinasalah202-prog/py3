import math
import sys

def starting(pos1):
    pos0 = (0, 0, 0)
    print(f"Position created: {pos1}")
    distance1 = float(round(math.sqrt((pos1[0] - pos0[0])**2 + (pos1[1] - pos0[1])**2 + (pos1[2] - pos0[2])**2)))
    print(f"Distance between {pos0} and {pos1}: {round(distance1, 2)}\n")

def parsing(coors):
    try:
        pos2 = tuple(coors.split(","))
        distance2= float(round(math.sqrt((pos2[0] - pos0[0])**2 + (pos2[1] - pos0[1])**2 + (pos2[2] - pos0[2])**2)))
        print(f"Parsed position: {pos2}")
        print(f"Distance between {pos0} and {pos2}: {round(distance2, 2)}")
    except Exception as e:
        print(f"Error parsing coordinate: {e}")
        print(f"Error details - Type: ValueError, Args: {e}\n")
    return pos2

def nUnpacking(p2):
    print("\nUnpacking demonstration:")
    print(f"Player at x={p2[0]}, y={p2[1]}, z={p2[2]}")
    print(f"Coordinates: X={p2[0]}, Y={p2[1]}, Z={p2[2]}")


def gameStart():
    print("=== Game Coordinate System ===")
    pos1 = (10, 20, 5)
    starting(pos1)
    print('Parsing coordinates: "3,4,0"')
    a = parsing("3,4,0")
    print('Parsing invalid coordinates: "abc,def,ghi"')
    parsing("abc,def,ghi")
    nUnpacking(a)

gameStart()
