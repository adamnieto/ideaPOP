$(document).ready(function(){
	$("#button").click(function(){
		function writeToFile(ideaText){
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    var fh = fso.CreateTextFile("c://Users/adamnieto/Desktop/ideaPOP/data.txt", 8, false, 0);
    fh.WriteLine(ideaText);
    fh.Close();
	}
		$("#mytextarea").val("");
		var arrayWords = [];
		var originalArray = $('#ideaBox').val().split(" ");
		var ideaText = $('#ideaBox').val();
		writeToFile(ideaText);
	});
});
