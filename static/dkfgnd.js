
function get(filenames){
	fetch('/api_filesIn')
	.then((response) => response.json())
	.then(function(data) {
		console.log(data);
		for (var i = 0; i < data.length; i++) {
			if (data[i]["filename"] == filenames){
				document.querySelector('.ok').innerHTML += `- size: ${data[i]["size"]}<br>`;
			}
		}
			
	});
}

