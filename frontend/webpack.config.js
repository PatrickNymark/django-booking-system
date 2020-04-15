const path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin')

const isDevelopment = process.env.NODE_ENV=== 'development';

module.exports = {
    context: __dirname,
    entry: './app/index.js',
    devtool: 'source-map',
    output: {
        filename: 'js/[name].[hash].js',
        path: path.join(__dirname, '/build/'),
        publicPath: '/'
    },
    module: {
        rules: [
            {
                enforce: 'pre',
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'eslint-loader',
                options: {
                    configFile: "./.eslintrc",
                    emitWarning: true
                }
            },
            {
                test: /\.js$/,
                use: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.s(a|c)ss$/,
                loader: [
                    isDevelopment ? 'style-loader' : MiniCssExtractPlugin.loader,
                    { 
                        loader: 'css-loader',
                        options: {
                            modules: true,
                            sourceMap: isDevelopment
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sourceMap: isDevelopment
                        }
                    }
                ]
            },
            {
                test: /\.(svg)(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'url-loader?limit=100000',
            },
            {
                test: /\.(jpg|png)?$/,
                loader: ['file-loader?name=i-[hash].[ext]'],
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Django React',
            template: './public/index.html'
        }),
        new BundleTracker({
            filename: 'webpack-stats.json'
        }),
        new MiniCssExtractPlugin({
            filename: 'css/[name]-[hash].css',
            chunkFilename: 'css/[id]-[hash].css'
        }),
        new CleanWebpackPlugin(),
    ],
    resolve: {
        extensions: ['.js', '.jsx', '.scss']
    }
}