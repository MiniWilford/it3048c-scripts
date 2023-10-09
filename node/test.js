// Path module
var path = require("path");


// Console.log usage
console.log("Hello World");

// Variable
var hello = "Hello from NodeJS variable!";
console.log(`Printing Variable 'hello': ${hello}`);

// Built in variables in NodeJS
console.log("Directory Name: " + __dirname);
console.log("Directory and file name: " + __filename);

// Path Functions
console.log("\nUsing path module: ");
console.log(`Hello from file ${path.basename(__filename)}`);

// Process args
console.log(`Process args: ${process.argv}`);