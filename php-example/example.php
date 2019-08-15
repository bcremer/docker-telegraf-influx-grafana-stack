<?php
require __DIR__ . '/vendor/autoload.php';

$statsd = new League\StatsD\Client();
$statsd->configure([
    'host'      => '127.0.0.1',
    'port'      => 8125,
    'namespace' => 'performance'
]);

$ops = 0;
$startTime = microtime(true);

pcntl_async_signals(true);
pcntl_signal(SIGINT, static function () use (&$ops, $startTime) {
    $runtime = microtime(true) - $startTime;
    $opsPerSecond = $ops / $runtime;
    echo PHP_EOL;
    echo "Runtime:\t${runtime} Seconds\n";
    echo "Ops:\t\t${ops} \n";
    echo "Ops/s:\t\t${opsPerSecond} \n";
    echo "Killed by Ctrl C\n";
    exit(0);
});

echo "Sending Random metrics. ctrc + c to stop\n";
while (true) {
    $time = random_int(100, 400); // 100-200ms
    $types = ['search', 'book', 'login', 'login'];
    $type = $types[random_int(0 , 3)];

    $statsd->increment('request.successful.count,type=' . $type);
    $statsd->timing('request.successful.time,type=' . $type, $time);
    ++$ops;

    usleep(random_int(5, 55) * 1000);
    echo '.';
}
