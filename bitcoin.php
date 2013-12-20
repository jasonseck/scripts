#!/usr/bin/env php
<?php

$c = curl_init();
curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($c, CURLOPT_HTTPHEADER, array('Accept: application/json', 'Content-Type: application/json'));
curl_setopt($c, CURLOPT_URL, 'http://data.mtgox.com/api/2/BTCUSD/money/ticker');

$data = curl_exec($c);
curl_close($c);
$obj = json_decode($data);
echo "avg "; echo print_r($obj->{'data'}->{'avg'}->{'display_short'}."\n", true);
echo "buy "; echo print_r($obj->{'data'}->{'buy'}->{'display_short'}."\n", true);
echo "sell "; echo print_r($obj->{'data'}->{'sell'}->{'display_short'}."\n", true);

?>
