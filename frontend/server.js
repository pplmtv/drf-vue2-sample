const http = require('http');
const fs = require('fs').promises

const hostname = '127.0.0.1';
const port = 8080;

const server = http.createServer((req, res) => {
	// const url = "public" + req.url;
	res.statusCode = 200;
	// res.setHeader('Content-Type', 'text/plain');
	// res.end('Hello World\n');
	// fs.readFile(__dirname + "/index.html")
	fs.readFile("../templates" + "/index.html")
		.then(contents => {
			res.setHeader("Content-Type", "text/html");
			res.writeHead(200);
			res.end(contents);
		})
});

server.listen(port, hostname, () => {
	console.log('Server running');
});
