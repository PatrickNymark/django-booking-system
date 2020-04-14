const path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin')

const isDevelopment = process.env.NODE_ENV=== 'development';

console.log(isDevelopment)
module.exports = {
    context: __dirname,
    mode: 'development',
    entry: './app/index.js',
    devtool: 'source-map',
    output: {
        filename: 'js/[name].[hash].js',
        path: path.resolve('public'),
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
        new BundleTracker({
            filename: 'webpack-stats.json'
        }),
        // new CleanWebpackPlugin(),
        new MiniCssExtractPlugin({
            filename: 'css/[name]-[hash].css',
            chunkFilename: 'css/[id]-[hash].css'
        }),
        new HtmlWebpackPlugin({
            template: 'public/index.html'
        })
    ],
    resolve: {
        extensions: ['.js', '.jsx', '.scss']
    }
}