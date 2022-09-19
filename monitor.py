from mcstatus import JavaServer
import argparse

activePlayers = 0
players = 0

parser = argparse.ArgumentParser(description='Check the number of players on a Minecraft server.')
parser.add_argument("-ip", "--ip", help="IP address of the server", required=True)
parser.add_argument("-p", "--port", help="Port of the server", required=True)
parser.parse_args()

serverIP = parser.parse_args().ip
serverPort = parser.parse_args().port

def check_players():
    while True:
        server = JavaServer(serverIP, serverPort)
        status = server.status()
        activePlayers = status.players.online
        return int(activePlayers)

while True:
    activePlayers = check_players()
    if players > activePlayers:
        players = activePlayers
        print(f"Player left, there are now {players} players online")
    elif players < activePlayers:
        players = activePlayers
        print(f"Player joined, there are now {players} players online")