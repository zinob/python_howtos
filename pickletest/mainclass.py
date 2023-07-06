import pickle
import data_class
import sys

FILE_NAME = "justapickle.pickle"


def write_pickle():
    data  = data_class.host('host1', 1)

    with open(FILE_NAME, 'wb') as f:
        pickle.dump(data, f)
        print(data)

def read_pickle():
    with open(FILE_NAME, 'rb') as f:
        data = pickle.load(f)
        print(data)
        print("calling the change_ip method")
        data.change_ip()
        print(data)

if __name__ == "__main__":
    if sys.argv[1] == "read":
        read_pickle()
    elif sys.argv[1] == "write":
        write_pickle()
    else:
        print("""Usage: python mainclass.py [read|write]
        
        used to demonstrate what changes in behavior when changing process_class.py between reads of the pickle file.
        try running this script first with write to create the file, then woth read

        write: write the pickle file
        read: read the pickle file
        """)