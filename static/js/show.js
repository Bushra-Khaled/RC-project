const userNameShow = document.getElementById("userNameShow");
const userNameHeader = document.getElementById("UserNameHeader");
const logoutBtn2 = document.getElementById("logout");


const getUserNameShow = userNameShow.textContent
localStorage.setItem("userNameStorage", getUserNameShow);
const userNameStorage = localStorage.getItem("userNameStorage");
const setUserNameHeader = userNameHeader.innerHTML = userNameStorage;
if (setUserNameHeader !== "") {
    welcomeUser.innerHTML = "Hey " + setUserNameHeader;
    logoutBtn2.style.display= "block";
}
else { 
    window.location.href = "/";
}