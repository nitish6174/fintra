$('#result').html('<h3 class="text-center">Search results will be displayed here</h3>');

$('#search').click( function() {
	search($('#query').val(),$('#mode').val());
});

function search(query,mode)
{
	$('#recent_list').append('<div class="history_item" onclick="search(\''+query+'\',\''+mode+'\')">'+'('+mode+') '+query+'</div>');
	$.ajax({
		url: '',
		type: 'POST',
		data: {
			query: query,
			mode: mode
		},
		success: function(data) {
			var links = (JSON.parse(data))['links'];			
			$('#result').html('');
			if(links.length>0)
			{
				for(i=0;i<links.length;i++)
				{
					$('#result').append('<div><a href="'+links[i]+'" target="_blank">'+links[i]+'</a></div>');
				}
			}
			else
			{
				$('#result').html('<h4 class="text-center">No results found for this query</h4>');
			}
		}
	});
}