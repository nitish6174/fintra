$('#search').click( function() {
	$.ajax({
		url: '',
		type: 'POST',
		data: {
			query: $('#query').val(),
			mode: $('#mode').val()
		},
		success: function(data) {
			$('#result').html(data);
		}
	});
});