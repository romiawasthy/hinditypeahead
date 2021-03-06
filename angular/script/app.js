var app = angular.module('app', ['autocomplete']);

// the service that retrieves some movie title from an url
app.factory('MovieRetriever', function($http, $q, $timeout){
    var MovieRetriever = new Object();
  

    MovieRetriever.getmovies = function(i) {
        var moviedata = $q.defer();
        var movies = [];
        var responsePromise = $http({url:"http://localhost:8983/solr/suggest?spellcheck.build=true&suggest.count=2&suggest.dictionary=mySuggester&suggest=true&wt=json", method:"GET", params:{"suggest.q": i}} );
	   responsePromise.success(function(data, status, headers, config) {
                      //console.log(JSON.stringify(data));
                     // console.log("romi123214:" + JSON.stringify(data.suggest.mySuggester[i].suggestions));
                     angular.forEach(data.suggest.mySuggester[i].suggestions, function(value, key) {
                      //  console.log("romi" + JSON.stringify(value.term));
                        movies.push(JSON.stringify(value.term));
    });		
        });
      responsePromise.error(function(data, status, headers, config) {
                    console.error("Cannot connect to search service:" + status);
      });

               
				
				

   
    $timeout(function(){
      moviedata.resolve(movies);
    },1000);

    return moviedata.promise
  }

  return MovieRetriever;
});

app.controller('MyCtrl', function($scope, MovieRetriever){

  $scope.movies = MovieRetriever.getmovies("...");
  $scope.movies.then(function(data){
    $scope.movies = data;
  });

  $scope.getmovies = function(){
    return $scope.movies;
  }

  $scope.doSomething = function(typedthings){
   // console.log("Do something like reload data with this: " + typedthings );
    $scope.newmovies = MovieRetriever.getmovies(typedthings);
    $scope.newmovies.then(function(data){
      $scope.movies = data;
    });
  }

  $scope.doSomethingElse = function(suggestion){
   // console.log("Suggestion selected: " + suggestion );
  }

});
