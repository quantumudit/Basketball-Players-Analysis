# Importing libraries

import numpy as np
import warnings
warnings.filterwarnings('ignore')

# -- Years -- #

years = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
years_dict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

# -- Players -- #

players = ["Kobe Bryant","Joe Johnson","LeBron James","Carmelo Anthony","Dwight Howard","Chris Bosh","Chris Paul","Kevin Durant","Derrick Rose","Dwayne Wade"]
players_dict = {"Kobe Bryant":0,"Joe Johnson":1,"LeBron James":2,"Carmelo Anthony":3,"Dwight Howard":4,"Chris Bosh":5,"Chris Paul":6,"Kevin Durant":7,"Derrick Rose":8,"Dwayne Wade":9}


# -- Player Salaries -- #

kobe_bryant_salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
joe_Johnson_salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
lebron_james_salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
carmelo_anthony_salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
dwight_howard_salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
chris_bosh_salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
chris_paul_salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
kevin_durant_salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
derrick_rose_salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
dwayne_wade_salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]

# -- Player Salary Matrix -- #

salary = np.array([kobe_bryant_salary, joe_Johnson_salary, lebron_james_salary, carmelo_anthony_salary, dwight_howard_salary, chris_bosh_salary, chris_paul_salary, kevin_durant_salary, derrick_rose_salary, dwayne_wade_salary])

# -- Games -- #

kobe_bryant_games = [80,77,82,82,73,82,58,78,6,35]
joe_Johnson_games = [82,57,82,79,76,72,60,72,79,80]
lebron_james_games = [79,78,75,81,76,79,62,76,77,69]
carmelo_anthony_games = [80,65,77,66,69,77,55,67,77,40]
dwight_howard_games = [82,82,82,79,82,78,54,76,71,41]
chris_bosh_games = [70,69,67,77,70,77,57,74,79,44]
chris_paul_games = [78,64,80,78,45,80,60,70,62,82]
kevin_durant_games = [35,35,80,74,82,78,66,81,81,27]
derrick_rose_games = [40,40,40,81,78,81,39,0,10,51]
dwayne_wade_games = [75,51,51,79,77,76,49,69,54,62]

#-- Games Matrix --#

games = np.array([kobe_bryant_games, joe_Johnson_games, lebron_james_games, carmelo_anthony_games, dwight_howard_games, chris_bosh_games, chris_paul_games, kevin_durant_games, derrick_rose_games, dwayne_wade_games])

# -- Minutes Played -- #

kobe_bryant_mp = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
joe_Johnson_mp = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
lebron_james_mp = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
carmelo_anthony_mp = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
dwight_howard_mp = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
chris_bosh_mp = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
chris_paul_mp = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
kevin_durant_mp = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
derrick_rose_mp = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
dwayne_wade_mp = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]

#-- Minutes Played Matrix --#

minutes_played = np.array([kobe_bryant_mp, joe_Johnson_mp, lebron_james_mp, carmelo_anthony_mp, dwight_howard_mp, chris_bosh_mp, chris_paul_mp, kevin_durant_mp, derrick_rose_mp, dwayne_wade_mp])

# -- Field Goals -- #

kobe_bryant_fg = [978,813,775,800,716,740,574,738,31,266]
joe_Johnson_fg = [632,536,647,620,635,514,423,445,462,446]
lebron_james_fg = [875,772,794,789,768,758,621,765,767,624]
carmelo_anthony_fg = [756,691,728,535,688,684,441,669,743,358]
dwight_howard_fg = [468,526,583,560,510,619,416,470,473,251]
chris_bosh_fg = [549,543,507,615,600,524,393,485,492,343]
chris_paul_fg = [407,381,630,631,314,430,425,412,406,568]
kevin_durant_fg = [306,306,587,661,794,711,643,731,849,238]
derrick_rose_fg = [208,208,208,574,672,711,302,0,58,338]
dwayne_wade_fg = [699,472,439,854,719,692,416,569,415,509]

# -- Matrix -- #

field_goals  = np.array([kobe_bryant_fg, joe_Johnson_fg, lebron_james_fg, carmelo_anthony_fg, dwight_howard_fg, chris_bosh_fg, chris_paul_fg, kevin_durant_fg, derrick_rose_fg, dwayne_wade_fg])

# -- Field Goal Attempts --#

kobe_bryant_fga = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
joe_Johnson_fga = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
lebron_james_fga = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
carmelo_anthony_fga = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
dwight_howard_fga = [881,873,974,979,834,1044,726,813,800,423]
chris_bosh_fga = [1087,1094,1027,1263,1158,1056,807,907,953,745]
chris_paul_fga = [947,871,1291,1255,637,928,890,856,870,1170]
kevin_durant_fga = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
derrick_rose_fga = [436,436,436,1208,1373,1597,695,0,164,835]
dwayne_wade_fga = [1413,962,937,1739,1511,1384,837,1093,761,1084]

# -- Field Goal Matrix --#

field_goal_attempts = np.array([kobe_bryant_fga, joe_Johnson_fga, lebron_james_fga, carmelo_anthony_fga, dwight_howard_fga, chris_bosh_fga, chris_paul_fga, kevin_durant_fga, derrick_rose_fga, dwayne_wade_fga])

# -- Points -- #

kobe_bryant_pts = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
joe_Johnson_pts = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
lebron_james_pts = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
carmelo_anthony_pts = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
dwight_howard_pts = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
chris_bosh_pts = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
chris_paul_pts = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
kevin_durant_pts = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
derrick_rose_pts = [597,597,597,1361,1619,2026,852,0,159,904]
dwayne_wade_pts = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]

# -- Points Matrix -- #

points = np.array([kobe_bryant_pts, joe_Johnson_pts, lebron_james_pts, carmelo_anthony_pts, dwight_howard_pts, chris_bosh_pts, chris_paul_pts, kevin_durant_pts, derrick_rose_pts, dwayne_wade_pts])