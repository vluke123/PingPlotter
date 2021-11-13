from pythonping import ping

'''
Commented out whilst trying to figure out how to get a constant output
from 'ping': set_interval = 0.25 set_count = float(input("For how long
(seconds) do you wish to plot your ping for?: ")) / set_interval
'''

tagret = "8.8.8.8"
count = 0
average_response_list = []

while True:
    print(f'count is {count}')
    response = ping(tagret, count=1, interval=0.25)
    count += 1
    print(f'{average_response_list}')
    average_response_list.append(response.rtt_min_ms)
    average_ms = round(sum(average_response_list) / count, ndigits=2)
    print(f'{response.rtt_min_ms} ms\nAverage = {average_ms}\n\
        Max ms = {max(average_response_list)}')
