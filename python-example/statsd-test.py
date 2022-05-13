import statsd
from time import sleep
from random import randint, choice

c = statsd.StatsClient('localhost', 8125, prefix='performance')

while True:
    incr = randint( 1, 5 )
    timing = randint( 100, 400 )
    metric_type = choice(['A', 'B', 'C'])
    print( f"\radding metric: type: {metric_type}, incr: {incr}, timing {timing} ms", end="")
    c.incr(f'request.successful.count,type={metric_type}', incr)  # Increment counter
    c.timing(f'request.successful.time,type={metric_type}', timing )
    sleep( randint(5, 55) / 1000 )
