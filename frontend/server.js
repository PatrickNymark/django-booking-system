// // Webpack dev server
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config.js');
const express = require('express');
const compression = require('compression');
const path = require('path');
const httpProxy = require('http-proxy');
const API_HOST = process.env.API_HOST || '127.0.0.1:8000';

if (process.env.NODE_ENV === 'development') {
    new WebpackDevServer(webpack(config), {
        port: 3000,
        host: 'localhost',
        hot: true,
        open: true,
        proxy: {
            '/api**': {
                target: API_HOST,
                secure: false,
                changeOrigin: true
            }
        },
        historyApiFallback: true,
    }).listen(3000, '0.0.0.0', (err) => {
      if (err) {
        console.log(err);
      }

      console.log('Listening at 0.0.0.0:3000');
    });
}


if (process.env.NODE_ENV === 'production') {
	const app = express();
	const apiProxy = httpProxy.createProxyServer();

	app.use(express.static('build'));

	app.use(compression());

	// Proxy all the api requests
	app.get('/api/*', function (req, res) {
		console.log('called')
		apiProxy.web(req, res, { target: 'http://' + API_HOST })
	});

	app.get('*', (req, res) => {
		res.sendFile(path.resolve(__dirname,  'build', 'index.html'));
	}); 

	PORT = 3000;

	app.listen(PORT)

	console.log(`Server running on ${PORT}`)

}