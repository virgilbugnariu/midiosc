import argparse
import mido.backends.rtmidi
from Learn import Learn
from src.Start import Start
from Connection import Connection

def main():
    parser = argparse.ArgumentParser(description="Test")
    parser.add_argument("-l", "--learn", action="store_true", help="Learn")
    parser.add_argument("-s", "--start", action="store_true", help="Start")
    parser.add_argument("-c", "--connection", action="store", help="Save connection address")
    args = parser.parse_args()
    
    if args.learn:
        inst = Learn()
    
    if args.start:
        inst = Start()

    if args.connection:
        inst = Connection(args.connection)

    inst.init()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error", e)