(function() {
    'use strict';
    var app = angular.module('ifroosnApp', ['chart.js']);
    app.controller('FetchController', ['$scope', '$http', function($scope, $http) {
        $scope.buss = {
            id: ''
        };
        $scope.fetchData = function() {
            console.log('heya');
            console.log('=> ' + $scope.buss);
            $http.get('http://localhost:8000/fetch', $scope.buss).then(function(res) {
                $scope.fetchedData = res.data;
                console.log('[SUCCESS] ' + res);
            },function(err) {
                console.log('[ERROR] ' + err);
            });
        };

        for(var i = 0; i < $scope.fetchedData.)

        $scope.labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
        $scope.series = ['Series A'];
        $scope.data = [
            [65, 59, 80, 81, 56, 55, 40]
        ];
    }]);
})();