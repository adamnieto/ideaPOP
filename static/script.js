$(document).ready(function(){
	$("#button").click(function(){
		$("#mytextarea").val("");
		var arrayWords = [];
		var originalArray = $('#ideaBox').val().split(" ");
		for (i = 0; i < originalArray.length; ++i) {
			if("*" == originalArray[i][0]) {
				arrayWords.push(originalArray[i]);
			}
		}
		var word;
		for(word = 0; word < arrayWords.length; ++word) {
			$("#images").empty();
			$("#mytextarea").text($("#mytextarea").val() + " " + arrayWords[word]);
			$.getJSON("http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?", {
				tags: arrayWords[word],
				tagmode: "any",
				format: "json"
			}, function(data){
				$.each(data.items, function(i, item){
					$('<img class="img-circle">').attr("src", item.media.m).appendTo('#images');
					if(i===0) {
						return false;
					}
				});		
			});
		}
	});


});

