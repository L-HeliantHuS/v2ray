import sys
import json
import uuid

path = "/etc/v2ray/config.json"


def readJsonFile() -> dict:
    with open(path, "r") as fp:
        return json.loads(fp.read())


def writeJsonFile(data: dict):
    data = json.dumps(data)

    with open(path, "w") as fp:
        fp.seek(0, 0)
        fp.write(data)


def execCommands(command: str):
    # Show all users
    if command == "all":
        data = readJsonFile()["inbounds"][0]["settings"]["clients"]
        for i in data:
            print(i)

    # New user
    if command == "new":

        injectData = {
            "id": str(uuid.uuid4()),
            "level": 1,
            "alterId": 5478
        }

        print("To be written data is: ")
        print(injectData)

        userInput = input("Writed? (Y/n)").lower()
        if userInput == "n":
            print("all right, no writed.")
            exit()

        data = readJsonFile()
        data["inbounds"][0]["settings"]["clients"].append(injectData)

        writeJsonFile(data)

        print()

        print("Writed success!  data is : %s, alterId is: %d" % (injectData["id"], injectData["alterId"]))

    # Delete user
    if command == "del":
        data = readJsonFile()
        delUUID = input("uuid: ")
        delIndex = -1

        for index, i in enumerate(data["inbounds"][0]["settings"]["clients"]):
            if i["id"] == delUUID:
                delIndex = index

        if delIndex == -1:
            print("Not find the UUID, please check input")
            exit()

        del data["inbounds"][0]["settings"]["clients"][delIndex]

        writeJsonFile(data)

        print("Deleted! data is : %s" % delUUID)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Not Right Used!")
        print("""
            Example:
                python3 v2ray.py all    ->   Show All Users
                
                python3 v2ray.py new    ->   New 1 User
                
                python3 v2ray.py del    ->   Del 1 User
                
                xD?
        """)
        exit()

    command = sys.argv[len(sys.argv) - 1]

    execCommands(command)
