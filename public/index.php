<?php

require '/var/www/vendor/autoload.php';

header("refresh: 0.3");
ob_start();
phpinfo();

$data = ob_get_contents();
ob_get_clean();


echo $data;

$connection = new MongoDB\Client("mongodb://root:pass@mongo:27017");

$db = $connection->prjctr;
$collection = $db->content;

do {
    $collection->insertOne(['data' => $data]);
    $allData = $collection->find();
} while (true);
