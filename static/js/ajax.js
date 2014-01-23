$(document).ready(function() {
	
	$(".user-data").on("click", "#delete", function(e) {
		if(window.confirm("Are you sure you want to delete this user?")) {
			var user_id;
			user_id = $(this).attr("user-id");
			url = '/delete_user/' + user_id + '/'
			$.ajaxSetup({
				beforeSend: function(xhr, settings) {
					function getCookie(name) {
						var cookieValue = null;
						if (document.cookie && document.cookie != '') {
							var cookies = document.cookie.split(';');
							for (var i = 0; i < cookies.length; i++) {
								var cookie = jQuery.trim(cookies[i]);
								// Is this the correct cookie
								if (cookie.substring(0, name.length + 1) == (name + '=')) {
									cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
									break;
								}
							}
						}
						return cookieValue;
					}
					if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
					    // Only send the token to relative URLs i.e. locally.
					    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
					}
				}
			});

			$.post(url)
			/* add in ajax request */
			$(e.target).closest('div').hide();
		}
	});
});