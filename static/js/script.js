const userName = document.getElementById("userName");
const welcomeUser = document.getElementById("welcomeUser");
const logoutBtn = document.getElementById("logout");
const session= localStorage.getItem("userSession");

//save the logged in user in local storage
function get_user(){
    const userSession = userName.value;
    localStorage.setItem("userSession", userSession);
}
// remove the user from local storage on logout
function remove_user(){
    localStorage.clear();
}

// show / hide the welcome user and log out from nav bar when the user logged in/out.
if (session == null) {
    welcomeUser.style.display= "none";
    logoutBtn.style.display= "none";
}
else {
    welcomeUser.innerHTML = "Hey " + session;
}

// show / hide message box "the message that's sent from the backend on any action of the user"
const msg=document.getElementById("msg");
if (msg.textContent !== "" ) {
    msg.style.display ="block";
}
else {
    msg.style.display ="none";
}
