#!/usr/bin/env python2


class Game(object):

  #date
  @property
  def date(self):
    return self._date

  @date.setter
  def date(self, value):
    self._date = value

  # teams
  @property
  def team_a(self):
    return self._team_a

  @team_a.setter
  def team_a(self, value):
    self._team_a = value

  @property
  def team_b(self):
    return self._team_b

  @team_b.setter
  def team_b(self, value):
    self._team_b = value

  #outer score
  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if (value == None):
      self._score = None
    else:
      self._score = {}
      self._score['a'] = value[0]
      self._score['b'] = value[1]
      self._score['in_prime_time'] = value[2]

  def team_a_points(self):
    if (self.score['a'] > self.score['b']):
      if (self.score['in_prime_time']):
        return 3
      else:
        return 2
    else:
      if (not self.score['in_prime_time']):
        return 1
      else:
        return 0

  def team_b_points(self):
    if (self.score['b'] > self.score['a']):
      if (self.score['in_prime_time']):
        return 3
      else:
        return 2
    else:
      if (not self.score['in_prime_time']):
        return 1
      else:
        return 0

  def __init__(self, team_a, team_b, score = {}):
    self.team_a = team_a
    self.team_b = team_b
    self.score = score

  def __str__(self):
    string = "Game between " + str(self.team_a) + " and " + str(self.team_b)
    if (self.score != None):
      string += " (" + str(self.score['a']) + ":" + str(self.score['b'])
      if (self.score['in_prime_time']):
        string += " in prime time"
      else:
        string += " in added time"
      string += ")"
    return string


class Team(object):
  def __init__(self, name):
    self.name = name

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  def __str__(self):
    return self.name

  def __cmp__(self, other):
    return cmp(self.name, other.name)


class Group(object):
  def __init__(self, name):
    self._name = name

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  @property
  def teams(self):
    return sorted(self._teams)

  @teams.setter
  def teams(self, value):
    self._teams = value

  def __str__(self):
    string = "Group " + self.name + " ["
    string += ', '.join("'" + str(team) + "'" for team in self.teams)
    string += "]"

    return string


class Championship(object):
  @property
  def teams(self):
    return self._teams

  @teams.setter
  def teams(self, value):
    self._teams = value

  @property
  def groups(self):
    return self._groups

  @groups.setter
  def groups(self, value):
    self._groups = value

  @property
  def games(self):
    return self._games

  @games.setter
  def games(self, value):
    self._games = value


  def __init__(self):
    self.teams = []
    self.groups = {}
    self.games = {}

  def init_group(self, name, teams):
    group = Group(name)
    group.teams = teams

    self.groups[name] = group
    for team in teams:
      self.teams.append(team)

  def __str__(self):
    string = "Championship\n"
    string += "Teams:\n"
    counter = 1
    for team in self.teams:
      string += str(counter) + ". " + str(team) + "\n"
      counter += 1
    string += "Groups:\n"
    counter = 1
    for key in self.groups:
      string += str(counter) + ". " + str(self.groups[key]) + "\n"
      counter += 1
    string += "Games:\n"
    for key in self.games:
      string += key + ": " + str(self.games[key]) + "\n"
    return string

  def add_game_info(self, game):
    if (game.team_a in self.teams and game.team_b in self.teams):
      id = ':'.join(str(team) for team in sorted([game.team_a, game.team_b]))
      self.games[id] = game
    else:
      raise Exception('One of teams is invalid')

  def group_statistics(self, group_name):
    group_table = []
    group = self.groups[group_name]
    for team in group.teams:
      group_table.append(self.team_statistics(team))
    return group_table

  def team_statistics(self, team):
    statistics = TeamStatistics(team)
    for key in self.games:
      game = self.games[key]
      if (game.team_a == team):
        statistics.add_game_statistics({'goals_for':game.score['a'], 'goals_against':game.score['b'], 'points':game.team_a_points()})
      elif (game.team_b == team):
        statistics.add_game_statistics({'goals_for':game.score['b'], 'goals_against':game.score['a'], 'points':game.team_b_points()})
    return statistics

  def print_group(self, group_name):
    statistics = sorted(self.group_statistics(group_name), reverse = True)
    for team in statistics:
      print team

class TeamStatistics(object):
  def __init__(self, team):
    self.team          = team
    self.games_played  = 0
    self.goals_for     = 0
    self.goals_against = 0
    self.points        = 0

  def __str__(self):
    string = "%-12s : %2s  %2s:%-2s  %2s" % (self.team, self.games_played, self.goals_for, self.goals_against, self.points)
#   str({'team':self.team, 'games_played':self.games_played, 'goals_for':self.goals_for, 'goals_against':self.goals_against, 'points':self.points})
    return string

  def __cmp__(self, other):
    if (self.points != other.points):
      return cmp(self.points, other.points)
    else:
      return cmp(self.goals_for - self.goals_against, other.goals_for - other.goals_against)

  @property
  def team(self):
    return self._team

  @team.setter
  def team(self, value):
    self._team = value

  @property
  def games_played(self):
    return self._games_played

  @games_played.setter
  def games_played(self, value):
    self._games_played = value

  @property
  def goals_against(self):
    return self._goals_against

  @goals_against.setter
  def goals_against(self, value):
    self._goals_against = value

  @property
  def goals_for(self):
    return self._goals_for

  @goals_for.setter
  def goals_for(self, value):
    self._goals_for = value

  @property
  def points(self):
    return self._points

  @points.setter
  def points(self, value):
    self._points = value

  def add_game_statistics(self, params):
    self.games_played  += 1
    self.goals_for     += params['goals_for']
    self.goals_against += params['goals_against']
    self.points        += params['points']


championship2014 = Championship()

championship2014.init_group('A', ['Canada', 'Czech', 'Denmark', 'France', 'Italy', 'Norway', 'Slovakia', 'Sweden'])
championship2014.init_group('B', ['Belarus', 'Finland', 'Germany', 'Kazakhstan', 'Latvia', 'Russia', 'Switzerland', 'USA'])

#9 May
championship2014.add_game_info(Game('France',      'Canada',      [3,2,False]))
championship2014.add_game_info(Game('Switzerland', 'Russia',      [0,5,True]))
championship2014.add_game_info(Game('Slovakia',    'Czech',       [2,3,False]))
championship2014.add_game_info(Game('Belarus',     'USA',         [1,6,True]))
#10 May
championship2014.add_game_info(Game('Italy',       'Norway',      [0,3,True]))
championship2014.add_game_info(Game('Kazakhstan',  'Germany',     [1,2,False]))
championship2014.add_game_info(Game('Sweden',      'Denmark',     [3,0,True]))
championship2014.add_game_info(Game('Finland',     'Latvia',      [2,3,True]))
championship2014.add_game_info(Game('Canada',      'Slovakia',    [4,1,True]))
championship2014.add_game_info(Game('USA',         'Switzerland', [3,2,True]))
#11 May
championship2014.add_game_info(Game('France',      'Italy',       [1,2,True]))
championship2014.add_game_info(Game('Germany',     'Latvia',      [3,2,True]))
championship2014.add_game_info(Game('Norway',      'Denmark',     [4,3,True]))
championship2014.add_game_info(Game('Belarus',     'Kazakhstan',  [4,1,True]))
championship2014.add_game_info(Game('Sweden',      'Czech',       [4,3,False]))
championship2014.add_game_info(Game('Finland',     'Russia',      [2,4,True]))
#12 May
championship2014.add_game_info(Game('Slovakia',    'France',      [3,5,True]))
championship2014.add_game_info(Game('Switzerland', 'Belarus',     [3,4,True]))
championship2014.add_game_info(Game('Czech',       'Canada',      [3,4,True]))
championship2014.add_game_info(Game('Russia',      'USA',         [6,1,True]))
#13 May
championship2014.add_game_info(Game('Italy',       'Denmark',     [1,4,True]))
championship2014.add_game_info(Game('Germany',     'Finland',     [0,4,True]))
championship2014.add_game_info(Game('Norway',      'Sweden',      [1,2,True]))
championship2014.add_game_info(Game('Kazakhstan',  'Latvia',      [4,5,True]))
#14 May
championship2014.add_game_info(Game('Czech',       'Italy',       [2,0,True]))
championship2014.add_game_info(Game('Switzerland', 'Germany',     [3,2,True]))
championship2014.add_game_info(Game('Slovakia',    'Norway',      [5,2,True]))
championship2014.add_game_info(Game('Russia',      'Kazakhstan',  [7,2,True]))
#15 May
championship2014.add_game_info(Game('Canada',      'Denmark',     [6,1,True]))
championship2014.add_game_info(Game('USA',         'Latvia',      [5,6,True]))
championship2014.add_game_info(Game('Sweden',      'France',      [2,1,True]))
championship2014.add_game_info(Game('Finland',     'Belarus',     [2,0,True]))
#16 May
championship2014.add_game_info(Game('Canada',      'Italy',       [6,1,True]))
championship2014.add_game_info(Game('USA',         'Kazakhstan',  [4,3,False]))
championship2014.add_game_info(Game('Sweden',      'Slovakia',    [3,1,True]))
championship2014.add_game_info(Game('Finland',     'Switzerland', [3,2,False]))
#17 May
championship2014.add_game_info(Game('France',      'Norway',      [5,4,False]))
championship2014.add_game_info(Game('Latvia',      'Russia',      [1,4,True]))
championship2014.add_game_info(Game('Denmark',     'Czech',       [4,3,False]))
championship2014.add_game_info(Game('Belarus',     'Germany',     [5,2,True]))
championship2014.add_game_info(Game('Slovakia',    'Italy',       [4,1,True]))
championship2014.add_game_info(Game('Switzerland', 'Kazakhstan',  [6,2,True]))
#18 May
championship2014.add_game_info(Game('Canada',      'Sweden',      [3,2,False]))
championship2014.add_game_info(Game('USA',         'Finland',     [3,1,True]))
championship2014.add_game_info(Game('Czech',       'Norway',      [1,0,True]))
championship2014.add_game_info(Game('Russia',      'Germany',     [3,0,True]))

print 'Group A:'
championship2014.print_group('A')
print '\nGroup B:'
championship2014.print_group('B')

