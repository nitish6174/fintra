$('#search').click( function() {
	$.ajax({
		url: '',
		type: 'POST',
		data: {
			query: $('#query').val(),
			mode: $('#mode').val()
		},
		success: function(data) {
			var links = (JSON.parse(data))['links'];
			$('#result').html('');
			for(i=0;i<links.length;i++)
			{
				$('#result').append('<div><a href="'+links[i]+'">'+links[i]+'</a></div>');
			}
		}
	});
});