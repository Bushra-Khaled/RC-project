const userName = document.getElementById("userName");
const welcomeUser = document.getElementById("welcomeUser");
const logoutBtn = document.getElementById("logout");
const session= localStorage.getItem("userSession");

function get_user(){
    const userSession = userName.value;
    localStorage.setItem("userSession", userSession);
}

function remove_user(){
    localStorage.clear();
}

if (session == null) {
    welcomeUser.style.display= "none";
    logoutBtn.style.display= "none";
}
else {
    welcomeUser.innerHTML = "Hey " + session;
}
// show and hide message box
const msg=document.getElementById("msg");
if (msg.textContent !== "" ) {
    msg.style.display ="block";
}
else {
    msg.style.display ="none";
}

// const reqInput = document.getElementsByTagName("input['submit']");
// if (5 >2) {
//     console.log(reqInput)
// }

