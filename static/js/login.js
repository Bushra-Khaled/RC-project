const loginBtn = document.getElementById("login-btn");
const signupBtn = document.getElementById("signup-btn");
const loginForm = document.getElementById("login-form");
const signupForm = document.getElementById("signup-form");

// functions to disply or hide login form 
function loginFormShow(){
    loginForm.style.display= "block";
    signupForm.style.display = "none"
}

// functions to disply or hide signup form 
function signupFormShow(){
    signupForm.style.display = "block";
    loginForm.style.display= "none";
    
}

loginBtn.addEventListener("click", loginFormShow);
signupBtn.addEventListener("click", signupFormShow);