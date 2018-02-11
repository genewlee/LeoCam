<?php
    if(isset($_POST['action'])) {
	$DIR="/var/www/LeoStream/";
	$time="30";
	
	if($_POST['action'] == 'start') {
        	exec('node server.js . > /dev/null 2>&1 & TASK_PID=$!; sleep ' . $time . '; kill $TASK_PID');
		echo "closed";
	}

	if($_POST['action'] == 'post') {
		exec("/usr/bin/python {$DIR}postClient.py > /dev/null 2>&1 &");	
		echo $time;
	}
    }
?>
