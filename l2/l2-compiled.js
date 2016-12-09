var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

var jsdom = require('jsdom');
var fs = require('fs');
var jquery = fs.readFileSync("./jquery-3.1.1.min.js").toString();

jsdom.env({
    html: 'http://mosigra.ru/',
    src: [jquery],
    done: function (errors, window) {
        var $ = window.$;
        $('a').each(function () {
            console.log(' -', $(this).text());
        });
    }
});

//# sourceMappingURL=l2-compiled.js.map