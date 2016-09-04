
(function (){

    $(document).ready(function(){
        $('#new-link').submit(function (event){

            event.preventDefault();

            var link = $('input[name="link"]').val().trim();
            var tags = $('input[name="tags"]').val().split(',').map(function(e){
                return e.trim();
            });

            $.post('/api/links/', {'data': JSON.stringify({'link': link, 'tags': tags})});

        });

    });

}());
