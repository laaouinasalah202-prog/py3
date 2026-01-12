import math


def starting(pos1):
    """" implement the below equation
            math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)"""
    pos0 = (0, 0, 0)
    print(f"Position created: {pos1}")
    distance1 = float(
            math.sqrt(
                (pos1[0] - pos0[0])**2
                + (pos1[1] - pos0[1])**2
                + (pos1[2] - pos0[2])**2
                )
            )
    print(f"Distance between {pos0} and {pos1}: {round(distance1, 2)}\n")


def unpacking(coors):
    """ get the coordination from coors if fails raise error """
    pos0 = (0, 0, 0)
    try:
        pos2 = tuple(coors.split(","))
        distance2 = float(
                math.sqrt(
                    (int(pos2[0]) - int(pos0[0]))**2
                    + (int(pos2[1]) - int(pos0[1]))**2
                    + (int(pos2[2]) - int(pos0[2]))**2
                    )
                )
        print(f"Parsed position: {tuple(map(int, pos2))}")
        print(f"Distance between {tuple(map(int, pos0))} "
              f"and {tuple(map(int, pos2))}: {distance2}\n")
    except Exception as e:
        print(f"Error parsing coordinate: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}",)\n')
    return pos2


def nUnpacking(p2):
    """" display teleport point """
    print("\nUnpacking demonstration:")
    print(f"Player at x={p2[0]}, y={p2[1]}, z={p2[2]}")
    print(f"Coordinates: X={p2[0]}, Y={p2[1]}, Z={p2[2]}")


def gameStart():
    """" use privious functions in order to display all steps """
    print("=== Game Coordinate System ===\n")
    pos1 = (10, 20, 5)
    starting(pos1)
    print('Parsing coordinates: "3,4,0"')
    a = unpacking("3,4,0")
    print('Parsing invalid coordinates: "abc,def,ghi"')
    unpacking("abc,def,ghi")
    nUnpacking(a)


gameStart()
