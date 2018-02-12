<?php

$db = new PDO('sqlite:/home/pi/sandboxes/LeoCam/LeoStream/auth.db'); 

if(isset($_POST['verify'])) {
	$password_sha1 = sha1($_POST['verify']);

	$sql  = "SELECT password_sha1 ";
 	$sql .= "FROM passwd ";
  	$sql .= "WHERE password_sha1='$password_sha1';";

	$result = $db->query($sql);
	$row = $result->fetch(PDO::FETCH_ASSOC);
	
	if ($row) {
		echo "success";
	} else {
		echo "fail";
	}
}
?>
