import argparse

def demo() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help = "Enter an string", dest = "string", type = str)
    parser.add_argument(help = "Enter a int", dest = "int", type = int)
    parser.add_argument(help = "Enter a float", dest = "float", type = float)

    args = parser.parse_args()

    string = args.string
    int = args.int
    float = args.float

    print("the string is: ", string)
    print("that int is: ", int)
    print("the float is: ", float)

