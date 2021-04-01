
// everytime a checkbox is clicked get the values of all the checkboxes
// and update the score at the bottom
function update_score() {

	// gets the values of all the checked boxes
	var boxes_checked = []
	var all_boxes = document.querySelectorAll('input[type=checkbox]'); 
	var checked = document.querySelectorAll('input[type=checkbox]:checked');

	var total_weights = 0;
	var checked_weights = 0;
	var num_checked = 0;
	var num_q = 0;

	var redflag = true;


	for (var i = 0; i < checked.length; i++) {
		if (Number(checked[i].value) == -1) {
			redflag = false;
			continue
		}
		checked_weights += Number(checked[i].value);
		num_checked++;
	}

	for (var i=0; i<all_boxes.length; i++) {
		if (Number(all_boxes[i].value) == -1)
			continue
		total_weights += Number(all_boxes[i].value);
		num_q++;
	}

	// console.log("checked=" + checked_weights + "\ntotal=" + total_weights);
	var msg = "Weighted score: " + (checked_weights + 0.2 * total_weights).toFixed(2) +"/"+total_weights;
	// +20 for inperfection differential
	msg += " or " + (checked_weights / total_weights * 100 + 20).toFixed(2) + "%";

	if (redflag) {
		document.getElementById("score").innerHTML = "RED FLAG ALERT"
		document.getElementById("raw").innerHTML = "";
	}
	else if (checked_weights != 0) {
		document.getElementById("score").innerHTML = msg;
		document.getElementById("raw").innerHTML = "Raw score: " + num_checked +
			"/" + num_q + " or " + (num_checked/num_q *100).toFixed(2) + "%";
	}
	else {
		document.getElementById("score").innerHTML = "Weighted score: ";
		document.getElementById("raw").innerHTML = "Raw score: ";
	}
}

function login() {
	var pw = "noabgsplz";
	var input = document.getElementById("accesscode").value;

	if (pw != input) {
		document.getElementById("accesscode").value = "";
		alert("Access denied: contact admin for access");
	}
	else {
		console.log("success");
		document.getElementById("login").style.display = "none";
		document.getElementById("footer1").style.display = "none";

		document.getElementById("questions").style.display = "block";
		document.getElementById("score").style.display = "block";
		document.getElementById("raw").style.display = "block";

		document.getElementById("footer2").style.display = "block";

	}
}
