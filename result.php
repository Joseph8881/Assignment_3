<!DOCTYPE html>
<html>
<head>
    <title>Results</title>
</head>
<body>
<h2>Assignment #3 Results</h2>

<?php
$x = $_POST['x'];
$y = $_POST['y'];
$z = $_POST['z'];

$command = escapeshellcmd("python3 process_input.py $x $y $z");
$output = shell_exec($command);

echo $output;
?>

</body>
</html>
