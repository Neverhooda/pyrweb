function left_hand_up() {
    send_command("left_hand", "up", "10")
}

function left_hand_down() {
    send_command("left_hand", "down", "10")
}

function left_hand_reset() {
    send_command("left_hand", "reset", "0")
}

function right_hand_up() {
    send_command("right_hand", "up", "10")
}

function right_hand_down() {
    send_command("right_hand", "down", "10")
}

function right_hand_reset() {
    send_command("right_hand", "reset", "0")
}

function send_command(url, action, parameters) {
    var http = new XMLHttpRequest();
    var params = 'action=' + action + '&parameters=' + parameters;
    console.log(params);
    http.open('POST', url, true);
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
        }
    }
    http.send(params);
}