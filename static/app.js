new Vue({
    el: '#app_art_page',
    data: {
       articles: []
    },
    created: function (){
        const vm = this;
        axios.get('/api/comments/')
            .then(function (response){
                vm.articles = response.data
            })
    }
}
)