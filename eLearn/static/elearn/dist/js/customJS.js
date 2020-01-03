function readURL(input, IdName) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#'+IdName)
                .attr('src', e.target.result)
                .width(300)
                .height(200);
        };
        reader.readAsDataURL(input.files[0]);
    }
}
