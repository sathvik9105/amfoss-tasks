import requests
from bs4 import BeautifulSoup

def get_livescore():
    # URL of Espn live website
    url = "https://www.espncricinfo.com/live-cricket-score"

    # Sending an HTTP GET request to fetch content from the website
    response = requests.get(url)

    # Setting up variablesfor storing info
    teamA = ""
    teamB = ""
    status = ""

    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # finding the specific div element
        specific_div = soup.find('div', class_='ds-px-4 ds-py-3')

        if specific_div:
            # extracting team names
            team_names_div = specific_div.find_all('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
            
            if len(team_names_div) == 2:
                # Team A
                teamA_element = team_names_div[0].find('div', class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')
                if teamA_element:
                    teamA = teamA_element.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3').text.strip()

                # Team B
                teamB_element = team_names_div[1].find('div', class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')
                if teamB_element:
                    teamB = teamB_element.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate').text.strip()

            # Extract status
            status_element = specific_div.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')
            if status_element:
                status = status_element.text.strip()

    cricket_data = {
        "teamA": teamA,
        "teamB": teamB,
        "status": status,
    }