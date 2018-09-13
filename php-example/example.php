<?php
require __DIR__ . '/vendor/autoload.php';

$statsd = new League\StatsD\Client();
$statsd->configure([
    'host' => '127.0.0.1',
    'port' => 8125,
    'namespace' => 'performance'
]);


echo "Sending Random metrics. ctrc + c to stop\n";
while (true) {
    $time = random_int(100, 400); // 100-200ms
    $types = ['search', 'book', 'login'];
    $type = $types[random_int(0 , 2)];

    $statsd->increment('request.successful.count,type=' . $type);
    $statsd->timing('request.successful.time,type=' . $type, $time);

    usleep(random_int(5, 55) * 1000);
    echo '.';
}
