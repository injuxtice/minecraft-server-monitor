from mcstatus import JavaServer
import argparse

activePlayers = 0
players = 0
checkServer = False

parser = argparse.ArgumentParser(description='Check the number of players on a Minecraft server.')
parser.add_argument("-ip", "--ip", help="IP address of the server", required=True, type=str)
parser.add_argument("-port", "--port", help="Port of the server", required=True, type=int)
parser.parse_args()

serverIP = parser.parse_args().ip
serverPort = parser.parse_args().port

def check_players():
    while True:
        server = JavaServer(serverIP, serverPort)
        status = server.status()
        activePlayers = status.players.online
        return int(activePlayers)

#if name is main
if __name__ == "__main__":
    print("Checking server status...")
    while True:
        try:
            activePlayers = check_players()
            if checkServer == False:
                print("Server is online! Server has " + str(activePlayers) + " players online. Script will update when player joins/leaves")
                checkServer = True
            if players > activePlayers:
                players = activePlayers
                print(f"Player left, there are now {players} players online")
            elif players < activePlayers:
                players = activePlayers
                print(f"Player joined, there are now {players} players online")
        except Exception:
            print("Server is offline")