$(document).ready(function(){
	var ShowForm = function(){
        var btn = $(this);
        var html_form = btn.attr("data-url");
		$('#modal-attendee').modal('show');
        $('#modal-attendee .modal-content').html(html_form);
		// $.ajax({
		// 	url: btn.attr("data-url"),
		// 	type: 'get',
		// 	dataType:'json',
		// 	beforeSend: function(){
		// 		$('#modal-book').modal('show');
		// 	},
		// 	success: function(data){
		// 		$('#modal-book .modal-content').html(data.html_form);
		// 	}
		// });
    };

    var SaveForm =  function(){
		var form = $(this);
		var fname = $('#fname').val()
		var mname = $('#mname').val()
		var lname = $('#lname').val()
		var phone = $('#phone').val()
		var email = $('#email').val()
		var token = "Token "+ Tk;
		data = {
			"first_name" : fname,
			"middle_name" : mname,
			"last_name" : lname,
			"phone_number" : phone,
			"email" : email,

		};
		console.log(data);
		console.log(token);
		$.ajax({
			url: form.attr('data-url'),
			data: data,
			type: form.attr('method'),
			dataType: 'json',
			beforeSend: function(request) {
				request.setRequestHeader("Authorization", token);
			  },
			success: function(data){
				console.log(data);
				$.ajax({
					url: attendees_url,
					type: 'GET',
					success: function(data){
						console.log(data);
						location.reload();
						// form.submit();
						// $("#dataTable tbody").html(data);
					}
				});
				$('#modal-attendee').modal('hide');
			}
		})
		return false;
    }
    
// create 
$(".show-form").click(ShowForm);
$("#modal-attendee").on("submit",".create-form",SaveForm);

//update
$('#book-table').on("click",".show-form-update",ShowForm);
$('#modal-book').on("submit",".update-form",SaveForm)

//delete
$('#modal-attendee').on("click",".show-form-delete",ShowForm);
$('#modal-book').on("submit",".delete-form",SaveForm)

});

