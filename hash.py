import copy
import numpy as np

ia = 'a_example.in'
ib = 'b_should_be_easy.in'
ic = 'c_no_hurry.in'
id = 'd_metropolis.in'
ie = 'e_high_bonus.in'
chosen = ie
finput=open(chosen)
rows, columns, vehicles, ride_no, bonus, steps = map(int, finput.readline().split())
# for each ride
rides = []
for i in range(ride_no):
    ride = map(int, finput.readline().split())
    (r_from, c_from, r_to, c_to, time_start, time_to) = ride
    rides.append((i, r_from, c_from, r_to, c_to, time_start, time_to))

assert finput.readline() == ''

# sort all rides by their earliest time
rides = sorted(rides, key=lambda x:x[5], reverse=True)
print 'sorted', rides
# TODO clever sort by x==y to make search easier

# create a series of times which keeps track when which cars are available
timeseries = [[] for x in list(range(steps))]
myvehs = [(vehicle, 0, 0) for vehicle in range(vehicles)]
# initially all cars are available
timeseries[0].extend(myvehs)

def dst(p1, p2):
    return abs((p1[0] - p2[0])) + abs((p1[1] - p2[1]))

# record journeys
journeys = [[] for car in range(vehicles)]

# basically simulate over time
time = 0
for av_vehs in timeseries:
    print 'time', time
    if av_vehs == []:
        time += 1
        continue
    #timeseries[3].append((0, 5,5))
    print 'av vehs', av_vehs
    # find the next ride that the vehicle can do
    for veh in av_vehs[::-1]:
        print 'veh', veh
        for ride in rides[::-1]:
           #print 'ride', ride
           time_to_get_to_ride = dst((veh[1], veh[2]), (ride[1], ride[2]))
           dst_to_drive = dst((ride[1], ride[2]), (ride[3], ride[4]))

           # cannot add if it's finished
           if time_to_get_to_ride + dst_to_drive > len(timeseries):
               continue

           # if there is enough time to finish, go for it
           if dst_to_drive + time_to_get_to_ride < ride[6]:
               #print 'found a ride, overall cost', time_to_get_to_ride + dst_to_drive
               # send the car
               journeys[veh[0]].append(ride[0])
               # put the car back at the end of the journey
               # FIXME needs to use the time earley of time to get there, which ever first
               timeseries[time_to_get_to_ride + dst_to_drive].append((veh[0], ride[3], ride[4]))
               del rides[rides.index(ride)]
               del av_vehs[av_vehs.index(veh)]
               break
    time += 1

output = open(chosen + '.out', 'w')
for jour in journeys:
    output.write(str(len(jour)) + ' ' + ' '.join(map(str, jour)) + '\n')
