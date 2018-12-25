import pandas as pd
import requests
import math
# import matplotlib.pyplot as plt


def correct_position(pos):
    posits = {'MLB': 'ILB',
              'C/RG': 'C',
              'FL': 'WR',
              'LB/MLB': 'ILB',
              'RB/RS': 'RS',
              'LT/RT': 'T',
              'HB/ST': 'ST',
              'RG': 'G',
              'DT/LDT/NT': 'DT',
              'LB/LILB': 'ILB',
              'K': 'ST',
              'P': 'ST',
              'PR': 'ST',
              'RT/T': 'T',
              'LCB/RCB': 'CB',
              'FB/RB': 'RB',
              'DT/LDT': 'DT',
              'FB/WR': 'WR',
              'RS': 'FS',
              'LG/LT': 'T',
              'LCB': 'CB',
              'NT': 'DT',
              'FL/WR': 'WR',
              'LOLB': 'OLB',
              'LDT/RDT': 'DT',
              'OG': 'G',
              'DT/RDT': 'DT',
              'LILB/MLB': 'ILB',
              'DE/LOLB': 'DE',
              'CB/LCB/RCB': 'CB',
              'LB/LOLB': 'OLB',
              'LB/RILB': 'ILB',
              'DT/NT': 'DT',
              'TE/WR': 'TE',
              'LT': 'T',
              'KR': 'RS',
              'FS/S': 'FS',
              'DE/DT': 'DE',
              'ROLB': 'OLB',
              'CB/LCB': 'CB',
              'LCB/SS': 'CB',
              'LDT/NT': 'DT',
              'DE/LDT': 'DE',
              'RB/TB': 'RB',
              'DE/LB': 'DE',
              'RCB': 'CB',
              'LILB': 'ILB',
              'DT/LDT/NT/RDT': 'DT',
              'DB/RCB': 'CB',
              'LOLB/ROLB': 'OLB',
              'LT/WR': 'T',
              'S': 'FS',
              'LB/LILB/MLB': 'ILB',
              'LDT': 'DT',
              'LB/ROLB': 'OLB',
              'WR/RS': 'RS',
              'LB/LOLB/SS': 'OLB',
              'RT': 'T',
              'SP': 'ST',
              'DE/DT/LDT': 'DT',
              'CB/DB/LCB/RCB': 'CB',
              'CB/RCB': 'CB',
              'LB': 'ILB',
              'LS': 'ST',
              'DB': 'CB',
              'RDT': 'DT',
              'FS/SS': 'FS',
              'MLB/RILB': 'ILB',
              'CB/ST': 'ST',
              'LG': 'G',
              'LB/LOLB/ROLB': 'OLB'
              }
    if pos in posits:
        return posits[pos]
    else:
        return pos


def name_to_abbr(name):
    all_teams = {
        'St. Louis Rams': 'STL',
        'San Diego Chargers': 'SDG',
        'Philadelphia Eagles': 'PHI',
        'New England Patriots': 'NWE',
        'Kansas City Chiefs': 'KAN',
        'New Orleans Saints': 'NOR',
        'Pittsburgh Steelers': 'PIT',
        'Oakland Raiders': 'OAK',
        'Los Angeles Rams': 'LAR',
        'Los Angeles Chargers': 'LAC',
        'Seattle Seahawks': 'SEA',
        'Buffalo Bills': 'BUF',
        'San Francisco 49ers': 'SFO',
        'Houston Texans': 'HOU',
        'Atlanta Falcons': 'ATL',
        'Minnesota Vikings': 'MIN',
        'Cincinnati Bengals': 'CIN',
        'Indianapolis Colts': 'IND',
        'Arizona Cardinals': 'ARI',
        'Green Bay Packers': 'GNB',
        'Miami Dolphins': 'MIA',
        'Dallas Cowboys': 'DAL',
        'Tennessee Titans': 'TEN',
        'Washington Redskins': 'WAS',
        'Carolina Panthers': 'CAR',
        'Detroit Lions': 'DET',
        'Jacksonville Jaguars': 'JAX',
        'Tampa Bay Buccaneers': 'TAM',
        'Baltimore Ravens': 'BAL',
        'Denver Broncos': 'DEN',
        'Cleveland Browns': 'CLE',
        'New York Giants': 'NYG',
        'Chicago Bears': 'CHI',
        'New York Jets': 'NYJ',
        'Two Teams': '2TM'
    }
    if name in all_teams:
        return all_teams[name]
    else:
        return name


def new_team_dic(year):
    return {
        'PHI' + str(year): {},
        'NWE' + str(year): {},
        'KAN' + str(year): {},
        'NOR' + str(year): {},
        'PIT' + str(year): {},
        'OAK' + str(year): {},
        'LAR' + str(year): {},
        'LAC' + str(year): {},
        'SEA' + str(year): {},
        'BUF' + str(year): {},
        'SFO' + str(year): {},
        'HOU' + str(year): {},
        'ATL' + str(year): {},
        'MIN' + str(year): {},
        'CIN' + str(year): {},
        'IND' + str(year): {},
        'ARI' + str(year): {},
        'GNB' + str(year): {},
        'MIA' + str(year): {},
        'DAL' + str(year): {},
        'TEN' + str(year): {},
        'WAS' + str(year): {},
        '2TM' + str(year): {},
        'CAR' + str(year): {},
        'DET' + str(year): {},
        'JAX' + str(year): {},
        'TAM' + str(year): {},
        'BAL' + str(year): {},
        'DEN' + str(year): {},
        'CLE' + str(year): {},
        'NYG' + str(year): {},
        'CHI' + str(year): {},
        'NYJ' + str(year): {},
        '2TM' + str(year): {}
    }


def add_playoff(dic, year):
    curr_html = ''
    next_html = ''
    curr_year_url = 'www.pro-football-reference.com/years/' + str(year) + '/playoffs.htm'
    next_year_url = 'www.pro-football-reference.com/years/' + str(year + 1) + '/playoffs.htm'
    curr_r = requests.get("http://" + curr_year_url)
    if hasattr(curr_r, 'text'):
        curr_html = curr_r.text

    next_r = requests.get("http://" + next_year_url)
    if hasattr(next_r, 'text'):
        next_html = next_r.text



    # print(curr_html)
    df_list = pd.read_html(curr_html)
    for i in range(len(df_list)):
        # print(len(df_list[i]))
        if list(df_list[i])[0] == 'Seed':
            # print(df_list[i].to_string())
            for j in range(len(df_list[i])):
                # print(df_list[i][1], type(df_list[i][1]))
                seed = df_list[i].iloc[j][0]
                team = df_list[i].iloc[j][1]
                if not math.isnan(seed):
                    # print(team, seed)
                    # print(name_to_abbr(team))
                    dic[name_to_abbr(team) + str(year)]['CYP'] = 1

    df_list = pd.read_html(next_html)
    for i in range(len(df_list)):
        # print(len(df_list[i]))
        if list(df_list[i])[0] == 'Seed':
            # print(df_list[i].to_string())
            for j in range(len(df_list[i])):
                # print(df_list[i][1], type(df_list[i][1]))
                seed = df_list[i].iloc[j][0]
                team = df_list[i].iloc[j][1]
                if not math.isnan(seed):
                    # print(team, seed)
                    # print(name_to_abbr(team))
                    # print(dic)
                    try:
                        dic[name_to_abbr(team) + str(year)]['NYP'] = 1
                    except KeyError:
                        print('\t' + team, seed)
                        print('\t' + name_to_abbr(team))
                        print('\t', dic)
                        if name_to_abbr(team) == 'SDG':
                            try:
                                dic['LAC' + str(year)]['NYP'] = 1
                            except KeyError:
                                print('ERROR')

                        continue

    return dic


def csv_analyze(year):
    team_dic = new_team_dic(year)
    df = pd.read_csv(str(year) + 'probowl.csv', sep=',')
    for index, row in df.iterrows():
        # print(row)
        team = row['Tm'] + str(year)
        pos = correct_position(row['Pos'])
        # if math.isnan(pos): continue
        if type(pos) == float: continue


        # if team already exists
        if team in team_dic:
            if pos in team_dic[team]:
                team_dic[team][pos] += 1
            else:
                team_dic[team][pos] = 1

        # if new team
        else:
            team_dic[team] = {pos: 1}

    # print(team_dic)
    print('--------------------------------------')
    return team_dic


def scrape_probowl(year):
    html = ''
    url = 'www.pro-football-reference.com/years/' + str(year) + '/probowl.htm'
    print(url)
    r = requests.get("http://" + url)
    if hasattr(r, 'text'):
        html = r.text

    df_list = pd.read_html(html)
    for i in range(len(df_list)):
        for j in range(len(df_list[i])):
            name = df_list[i].iloc[j][1]
            # print(name)
            if name[-1] == '%' or name[-1] == '+':
                df_list[i].iat[j, 1] = name[0:len(name) - 1]
                # print(df_list[i].iloc[j][1])

    for i, df in enumerate(df_list):
        # print(df.to_string())
        for j in range(len(df)):
            if df.iloc[j][0] not in positions:
                positions.append(df.iloc[j][0])
            if int(year) == 2018:
                pos_2018.append(df.iloc[j][0])

        # print(i)
        file_name = str(year) + 'probowl'
        df.to_csv('{}.csv'.format(file_name))
    print(year)


def main():
    filenames = []
    for year in range(2002, 2018):
        scrape_probowl(year)
        dic = csv_analyze(year)
        dic = add_playoff(dic, year)
        df = pd.DataFrame(dic).transpose().fillna(value=0)
        filename = str(year) + 'data.csv'
        df.to_csv(filename)
        filenames.append(filename)
    all_df = [pd.read_csv(f) for f in filenames]
    df1 = all_df[0]
    df2 = all_df[1]
    merged = pd.concat(all_df, ignore_index=True, sort=True).fillna(value=0)
    # mergedStuff = pd.merge(df1, df2,  how='outer')
    # cols = merged.columns.tolist()

    # cols = cols[-2:-1] + cols[0:2] + cols[3:9] + cols[10:-2] + cols[-1:] + cols[2:3] + cols[9:10]
    # print(type(cols), cols)

    # merged = merged[cols]
    # print(merged.to_string())

    merged.to_csv("alldata-unaltered.csv", index=False)


# 2008 and earlier are Different positions
data = []
positions = []
pos_2018 = []
if __name__ == '__main__':
    main()


