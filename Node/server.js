var http = require('http');
var fs = require ("fs");
var os = require ("os");
var ip = require("ip");

var seconds = os.uptime();
var minutes = seconds/60;
var hours = minutes/60;
var days = hours/24

seconds =  Math.floor(seconds);
minutes = Math.floor(minutes);
hours = Math.floor(hours);
days = Math.floor(days);

seconds = seconds%60;
minutes = minutes%60;
hours  = hours%24;


http.createServer(function (req, res){

    if(req.url === "/"){
        fs.readFile("./index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});    
        res.end(body);
    });
}
    
    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname();
        serverUptime=os.uptime();
        totalMemory=os.totalmem();
        freeMemory=os.freemem();
        cpus=os.cpus();
        html=`
        <!DOCTYPE html>
        <html>
            <head>
                <title>Node JS Response</title>
            </head>
            <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: ${days} Days, ${hours} hours, ${minutes} minutes, ${seconds} seconds. </p>
                <p>Total Memory: `+ os.totalmem()/1000000 +` mb</p>
                <p>Free Memory: `+ os.freemem/1000000 +` mb</p>
                <p>Number of CPUs: `+ os.cpus().length + ` </p>
            </body>
        </html>`
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type":"text/plain"})
        res.end('404 File Not Found At ${req.url}');
    }   
}).listen(3000);
console.log('Node.js web server listening on port 3000')