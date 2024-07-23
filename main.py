from flask import Flask, render_template, request
import random

app = Flask(__name__)

LOCATIONS = [
    "Mg auditorium", "Gazebo", "North Square", "admin Block", "Main Gate",
    "Mgr Circle", "Delta Block", "We mart", "Ab1", "Ab2", "Ab3",
    "Gymkhanna", "Basket Ball Court", "Aavin", "Health Centre"
]

def generate_team_paths(num_teams, locations, locations_per_team):
    team_paths = {}

    for team in range(1, num_teams + 1):
        path = random.sample(locations, locations_per_team)
        team_paths[team] = path

    return team_paths

def find_competitions(team_paths):
    competitions = {}
    for location in LOCATIONS:
        teams_at_location = [team for team, path in team_paths.items() if location in path]
        if len(teams_at_location) > 1:
            competitions[location] = teams_at_location
    return competitions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_teams = int(request.form['num_teams'])
        locations_per_team = 4  # Fixed number of locations per team

        # Generate team paths
        team_paths = generate_team_paths(num_teams, LOCATIONS, locations_per_team)

        # Find competitions
        competitions = find_competitions(team_paths)

        return render_template('results.html', team_paths=team_paths, competitions=competitions, num_teams=num_teams, num_locations=len(LOCATIONS))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)