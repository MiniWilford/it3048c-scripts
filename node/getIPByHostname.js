// Import DNS module
var dns = require('dns')

// Function to find hostname
function hostnameLookup(hostname) {
    dns.lookup(hostname, function(err, address, family) {
        console.log(address);
    })
}

// Check argv array length
if(process.argv.length <= 2) {
    console.log("Usage: " + __filename + " IPADDR");
    process.exit(-1);
}

var hostname = process.argv[2];
console.log(`Checking IP of ${hostname}`);
hostnameLookup(hostname);