$(document).ready(function() {
	
	$(".user-data").on("click", "#delete", function(e) {
		if(window.confirm("Are you sure?")) {
			e.preventDefault();
			var user_id;
			user_id = $(this).attr("user-id");
			console.log(user_id)
			url = '/delete_user/' + user_id
			$.get(url)
			/* add in ajax request */
			$(e.target).closest('div').hide();
		}
	});
});