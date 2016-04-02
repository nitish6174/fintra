$('#result').html('Results will be displayed here');

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
			if(links.length>0)
			{
				for(i=0;i<links.length;i++)
				{
					$('#result').append('<div><a href="'+links[i]+'">'+links[i]+'</a></div>');
				}
			}
			else
			{
				$('#result').html('No results found for this query.');
			}
		}
	});
});