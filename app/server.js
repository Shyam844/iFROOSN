var express = require('express');
// var path = require('path');
// var mysql = require('mysql');
// var http = require('http');
// var parser = require('body-parser');
var PythonShell = require('python-shell');

var router = express.Router();
var hostname = 'localhost';
var port = 8000;
var app = express();
// app.use(bodyParser.urlencoded({ extended: false }));
// app.use(bodyParser.json());

app.get('/fetch', function(req, res) {
    console.log(req.body);
    var businessId = 'gQtMGO7Yf_9cOksw66tHaA';
    console.log('[GET] Fetch Data');
    var pyshell = new PythonShell('scripts/dev/analysis/test.py');
    pyshell.send(businessId);
    pyshell.on('message', function (message) {
        res.json(message);
        console.log(message);
    });
});
app.listen(port, hostname, function() {
    console.log('Server is listening at http://' + hostname + ':' + port);
});