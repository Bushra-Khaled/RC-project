const welcomeUser = document.getElementById("welcomeUser");
const logoutBtn = document.getElementById("logout");

// remove the user from local storage on logout
logoutBtn.addEventListener("click", remove_user)
if(window.location.href == "/"){
    localStorage.clear();
    welcomeUser.style.display= "none";
    logoutBtn.style.display= "none";
}

function remove_user(){
    localStorage.clear();
    welcomeUser.style.display= "none";
    logoutBtn.style.display= "none";
    window.location.href = "/";
}

// show / hide message box "the message that's sent from the backend on any action of the user"
const msg=document.getElementById("msg");
if (msg.textContent !== "" ) {
    msg.style.display ="block";
}
else {
    msg.style.display ="none";
}

// confirmation before delete
const deleteBtns =document.getElementsByClassName("deleteBtn");
const entryIDs = document.getElementsByClassName("entryID");
for (let i = 0; i < deleteBtns.length; i++) {
    const x = entryIDs[i].textContent;
    deleteBtns[i].addEventListener("click", function() {
        confirmDelete(x);
    });
}
function confirmDelete(x){
    if (confirm ("Are you sure you want to delete this appointment")) {
       window.location.href =`/delete?id=${x}&userName=${userNameStorage}`;
    }
    else { 
    }
}

