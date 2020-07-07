
document.addEventListener('DOMContentLoaded', () => {

    // store session data in local browser storage
    let cart = `{{ cart }}`; 
    localStorage.setItem('cart', cart); 

    // listen for values to run submit function
    let username_button = document.querySelector('#username');
    let channel = document.querySelector('select');
    if (username_button) {
        username_button.addEventListener("keyup", submitFunction);
    };
    if (channel) {
        channel.addEventListener("change", submitFunction);
    };

    // function to enable register button if both values are inputted by user
    function submitFunction() {
        if (username_button.value === '' || channel.options[channel.selectedIndex].value == '') {
            document.querySelector('#submit').disabled = true;
        }
        else {
            document.querySelector('#submit').disabled = false;
            room = channel.options[channel.selectedIndex].value;
            username = username_button.value;
            localStorage.setItem('room', room);
            localStorage.setItem('username', username);
        }
    };

    // listen for new channel input on modal
    let channel_input = document.querySelector('#channel');
    if (channel_input) {
        channel_input.addEventListener("keyup", modalSubmit);
    };

    // if user enters a new channel name, enable modal submit button
    function modalSubmit() {
        if (channel_input.value == '') {
            document.querySelector('#modalsubmit').disabled = true;
        } else {
            document.querySelector('#modalsubmit').disabled = false;
        }
    };

    // scroll chatroom to bottom in case there's a lot of messages
    let messageBody = document.querySelector('#chatroom');
    if (messageBody) {
        messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
    };


    // trigger chat button click with enter key 
    input = document.querySelector('#chat');
    if (input) {
        input.addEventListener("keyup", event => {
            // Number 13 is the "Enter" key on the keyboard
            if (event.keyCode === 13) {
                document.querySelector('#send_chat').click();
            };
        });
    };


});