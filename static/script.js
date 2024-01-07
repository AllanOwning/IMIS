//Drag and drop feature for the wrapper.
document.getElementById('dragndrop-wrapper').addEventListener('dragover', function(e) {
 e.preventDefault();
});

document.getElementById('dragndrop-wrapper').addEventListener('drop', function(e) {
	e.preventDefault();
	let files = e.dataTransfer.files;
	if (files.length > 0) {
  	document.getElementById('dragndrop-input').files = files;
  	displayImage();
	}
});


//A function to display the images 
//within the drag and drop input field.
function displayImage() {
	let input = document.getElementById('dragndrop-input');

	if (input.files && input.files[0]) {
	    let reader = new FileReader();
	    let label = document.querySelector('label[for="dragndrop-input"]');
	    reader.onload = function(e) {
	     let image = document.getElementById('display-image');
	     image.src = e.target.result;
	     image.style.display = 'block';
	     label.style.display = 'none';
	    };
	    reader.readAsDataURL(input.files[0]);

	    //An event listener where it calls the reset button
	    //to clear the input of the uploaded image.
	    document.getElementById('reset-button').addEventListener('click', function() {
			document.getElementById('display-image').style.display = 'none';
			label.style.display = 'block';
		});
	  }
}

//A function to warn the user that 
//the drag and drop input field is
//empty.
function validateForm(){
	let input = document.getElementById('dragndrop-input');
 	if (!input.files || input.files.length === 0) {
	   alert('Please upload an image before submitting.');
	   return false;
 	}
 	return true;
}