var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${Math.floor(os.uptime() / 86400)}, Hours: ${Math.floor(os.uptime() / 3600)}, Minutes: ${Math.floor((os.uptime() / 60) % 60)}, Seconds: ${Math.floor(os.uptime() % 60)}</p>
            <p>Total Memory: ${Math.floor((os.totalmem() / 1024) / 1024)} MB</p>
            <p>Free Memory: ${Math.floor((os.freemem() / 1024) / 1024)} MB</p>
            <p>Number of CPUs: ${os.cpus().length}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");