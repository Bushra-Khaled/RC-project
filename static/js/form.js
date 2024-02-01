//shoe / hide update and book button
const entryID = document.getElementById("entryId");
const updateSec = document.getElementById("updateSec");
const bookSec = document.getElementById("bookSec");
if (entryID.value.length > 0 ){
    updateSec.style.display="inline-flex";
}
else {
    bookSec.style.display="block";
}

// set the appointment calendar to start available book from now
const appo = document.getElementById("appointment");
const max = "2050-01-28T17:46";
const timeElapsed = Date.now();
const now = new Date(timeElapsed);
const min = now.toISOString().slice(0, 16);
appo.min = min;
appo.max = max;
