<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    
    // Now you can process this data as you wish, such as sending an email, storing in a database, etc.
    // For demonstration purposes, let's just print the data:
    echo "Name: $name <br>";
    echo "Email: $email <br>";
    echo "Message: $message <br>";
    error_reporting(E_ALL);
    ini_set('display_errors', 1);

}
?>
