
// everytime a checkbox is clicked get the values of all the checkboxes
// and update the score at the bottom
function update_score() {

	// gets the values of all the checked boxes
	var boxes_checked = []
	var all_boxes = document.querySelectorAll('input[type=checkbox]'); 
	var checked = document.querySelectorAll('input[type=checkbox]:checked');

	var total_weights = 0;
	var checked_weights = 0;


	for (var i = 0; i < checked.length; i++) {
		// boxes_checked.push(checked[i].value);
		checked_weights += Number(checked[i].value);
	}

	for (var i=0; i<all_boxes.length; i++) {
		total_weights += Number(all_boxes[i].value);
	}

	// console.log("checked=" + checked_weights + "\ntotal=" + total_weights);
	var msg = "Score: " + checked_weights +"/"+total_weights;
	msg += " or " + (checked_weights / total_weights * 100).toFixed(2) + "%";
	document.getElementById("score").innerHTML = msg;

}
