import json
import requests

class DriverService:
    def __init__(self):
        pass

    # get all drivers of a year
    def getDriversOfYear(self, year):
        url = f"http://ergast.com/api/f1/{year}/drivers.json"
        response = requests.get(url)
        allDrivers = json.loads(response.text)
        return allDrivers["MRData"]["DriverTable"]["Drivers"]

    # get all gps of a year
    def getRacesOfYear(self, year):
        url = f"https://ergast.com/api/f1/{year}.json"
        response = requests.get(url)
        allRaces = json.loads(response.text)
        return allRaces["MRData"]["RaceTable"]["Races"]

    # get a single placement of a driver of a specific race
    def getSinglePlacement(self, year, driver, round):
        url = f"https://ergast.com/api/f1/{year}/{round}/drivers/{driver}/results.json"
        response = requests.get(url)
        placement = json.loads(response.text)
        if not placement['MRData']['RaceTable']['Races']: # if driver did not drive race return 0
            return 0
        else:
            return placement['MRData']['RaceTable']['Races'][0]['Results'][0]['position']

    # get all placements of a year of a specific driver
    def getAllPlacements(self, year, driver):
        url = f"https://ergast.com/api/f1/{year}/drivers/{driver}/results.json"
        response = requests.get(url)
        placement = json.loads(response.text)
        return placement['MRData']['RaceTable']['Races']