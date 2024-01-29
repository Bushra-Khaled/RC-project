//shoe / hide update and book button
const x = document.getElementById("entryId");
const y = document.getElementById("updateSec");
const z = document.getElementById("bookSec");
if (x.value.length > 0 ){
    y.style.display="inline-flex";
}
else {
    z.style.display="block";
}

// set the appointment calendar to start available book from now
const appo = document.getElementById("appointment");
const max = "2050-01-28T17:46";
const timeElapsed = Date.now();
const now = new Date(timeElapsed);
const min = now.toISOString().slice(0, 16);
appo.min = min;
appo.max = max;
