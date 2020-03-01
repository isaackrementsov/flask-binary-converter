function convert(binaryString, on_success){
    $.ajax({
        url: '/convert_binary',
        data: {
            binary_string: binaryString
        },
        dataType: 'json',
        type: 'get',
        success: function(response){
            on_success(response);
        }
    });
}

$('#convert-button').on('click', function(){
    let binaryString = $('#binary-input').val();

    convert(binaryString, function(decimal){
        $('#decimal').text(decimal);
        $('#decimal-container').show(200);
    });
});
