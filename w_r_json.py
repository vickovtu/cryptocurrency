import json
import time


file = 'file.json'


def write_rate(rate):
    while True:
        try:
            rate_json = json.dumps(rate)
            with open(file, 'w') as outfile:
                json.dump(rate, outfile, indent=4)
            print(f"==========={rate_json}=================")
        except Exception as e:
            print(e)
        time.sleep(2)



def read_rate(exchange):
    with open(file, "r") as read_file:
        data = json.load(read_file)
        return data[exchange]