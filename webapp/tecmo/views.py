from django.shortcuts import render
import random

###
### CONTROLLER
###

# called via Alexa skill
def vs_json():
    teams, tiers = _setup_teams_tomczak()
    tier, team1, team2 = _get_matchup(teams)

    response_dict = {}
    response_dict['tier'] = tier
    response_dict['team1'] = team1.name
    response_dict['team2'] = team2.name

    return tier, team1, team2

def index(request):
    context = {}
    return render(request, "tecmo/index.html", context)

def vs(request):
    tier_ranking = 'Tomczak'
    teams, tiers = _setup_teams_tomczak()
    tier, team1, team2 = _get_matchup(teams)

    context = {}
    context['tier'] = tier
    context['tier_ranking'] = tier_ranking
    context['team1'] = team1
    context['team2'] = team2
    return render(request, "tecmo/vs.html", context)

###
### PRIVATE
###

class Team(object):
    name = None
    id = -1
    tiers = []

    def __init__(self, name, img_id, tiers):
        self.name = name
        self.img_id = img_id
        self.tiers = tiers

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Tomczak rankings
# http://tecmotourney.blogspot.com/p/team-tiers.html
def _setup_teams_tomczak():
    teams = []

    # tier 1
    team = Team('49ers', 28, [1]) # 49ers
    teams.append(team)
    team = Team('Oilers', 10, [1]) # oilers
    teams.append(team)
    team = Team('Bills', 25, [1]) # bills
    teams.append(team)
    team = Team('Giants', 13, [1]) # giants
    teams.append(team)

    # tiers 1 & 2
    team = Team('Raiders', 7, [1, 2]) # raiders
    teams.append(team)

    # tier 2
    team = Team('Dolphins', 16, [2]) # dolphins
    teams.append(team)
    team = Team('Eagles', 15, [2]) # eagles
    teams.append(team)
    team = Team('Chiefs', 19, [2]) # chiefs
    teams.append(team)
    team = Team('Vikings', 1, [2]) # vikings
    teams.append(team)

    # tiers 2 & 3
    team = Team('Bears', 27, [2, 3]) # bears
    teams.append(team)
    team = Team('Rams', 6, [2, 3]) # rams
    teams.append(team)

    # tier 3
    team = Team('Redskins', 5, [3]) # redskins
    teams.append(team)
    team = Team('Bengals', 26, [3]) # bengals
    teams.append(team)
    team = Team('Broncos', 24, [3]) # broncos
    teams.append(team)
    team = Team('Chargers', 20, [3]) # chargers
    teams.append(team)

    # tiers 3 & 4
    team = Team('Falcons', 14, [3, 4]) # falcons
    teams.append(team)
    team = Team('Lions', 11, [3, 4]) # lions
    teams.append(team)

    # tier 4
    team = Team('Cowboys', 17, [4]) # cowboys
    teams.append(team)
    team = Team('Buccaneers', 22, [4]) # buccaneers
    teams.append(team)
    team = Team('Saints', 4, [4]) # saints
    teams.append(team)
    team = Team('Cardinals', 21, [4]) # cardinals
    teams.append(team)

    # tiers 4 & 5
    team = Team('Jets', 12, [4, 5]) # jets
    teams.append(team)
    team = Team('Steelers', 2, [4, 5]) # steelers
    teams.append(team)


    # tier 5
    team = Team('Browns', 23, [5]) # browns
    teams.append(team)
    team = Team('Packers', 9, [5]) # packers
    teams.append(team)
    team = Team('Seahawks', 3, [5]) # seahawks
    teams.append(team)
    team = Team('Colts', 18, [5]) # colts
    teams.append(team)
    team = Team('Patriots', 8, [5]) # patriots
    teams.append(team)

    return teams, 6

# experimental AGI rankings
def _setup_teams_agi():
    teams = []

    # tier 1
    team = Team('49ers', 28, [1]) # 49ers
    teams.append(team)
    team = Team('Oilers', 10, [1]) # oilers
    teams.append(team)
    team = Team('Bills', 25, [1]) # bills
    teams.append(team)
    team = Team('Giants', 13, [1]) # giants
    teams.append(team)

    # tiers 1 & 2
    team = Team('Raiders', 7, [1, 2]) # raiders
    teams.append(team)

    # tier 2
    team = Team('Dolphins', 16, [2]) # dolphins
    teams.append(team)
    team = Team('Eagles', 15, [2]) # eagles
    teams.append(team)
    team = Team('Chiefs', 19, [2]) # chiefs
    teams.append(team)
    team = Team('Bears', 27, [2]) # bears
    teams.append(team)

    # tiers 2 & 3
    team = Team('Lions', 11, [2, 3]) # lions
    teams.append(team)

    # tier 3
    team = Team('Vikings', 1, [3]) # vikings
    teams.append(team)
    team = Team('Rams', 6, [3]) # rams
    teams.append(team)
    team = Team('Redskins', 5, [3]) # redskins
    teams.append(team)

    # tiers 3 & 4
    team = Team('Falcons', 14, [3, 4]) # falcons
    teams.append(team)
    team = Team('Cowboys', 17, [3, 4]) # cowboys
    teams.append(team)

    # tier 4
    team = Team('Broncos', 24, [4]) # broncos
    teams.append(team)
    team = Team('Bengals', 26, [4]) # bengals
    teams.append(team)
    team = Team('Chargers', 20, [4]) # chargers
    teams.append(team)

    # tiers 4 & 5
    team = Team('Buccaneers', 22, [4, 5]) # buccaneers
    teams.append(team)

    # tier 5
    team = Team('Saints', 4, [5]) # saints
    teams.append(team)
    team = Team('Cardinals', 21, [5]) # cardinals
    teams.append(team)
    team = Team('Jets', 12, [5]) # jets
    teams.append(team)
    team = Team('Steelers', 2, [5]) # steelers
    teams.append(team)

    # tiers 5 & 6
    team = Team('Browns', 23, [5, 6]) # browns
    teams.append(team)

    # tier 6
    team = Team('Packers', 9, [6]) # packers
    teams.append(team)
    team = Team('Seahawks', 3, [6]) # seahawks
    teams.append(team)
    team = Team('Colts', 18, [6]) # colts
    teams.append(team)
    team = Team('Patriots', 8, [6]) # patriots
    teams.append(team)

    return teams, 6

def _roll_team(teams, tier=-1, not_team=-1):
    roll = random.randint(1,28)

    team = teams[roll-1]

    # if the team is not in the same tier, or is the same team already picked, find another
    while (tier != -1 and tier not in team.tiers) or team.img_id == not_team:
        roll = random.randint(1,28)
        #logger.info('backup team roll: ' + str(roll))
        team = teams[roll-1]
        #logger.info('backup team: ' + team.name)

    return team

def _get_matchup(teams):
    team1 = _roll_team(teams)
    tiers = team1.tiers
    idx = random.randint(0,len(tiers)-1)
    tier = team1.tiers[idx]
    team2 = _roll_team(teams, tier=tier, not_team=team1.img_id)
    return tier, team1, team2