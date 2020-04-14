// Webpack dev server
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const path = require('path');
const config = require('./webpack.config.js');

new WebpackDevServer(webpack(config), {
    port: 3000,
    host: 'localhost',
    hot: true,
    open: true,
    proxy: {
        '/api**': {
            target: 'http://localhost:8000',
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

