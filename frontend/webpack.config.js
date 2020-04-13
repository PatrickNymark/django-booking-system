const path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const isDevelopment = process.env.NODE_ENV=== 'development';


module.exports = {
    context: __dirname,
    mode: 'development',
    entry: './app/index.js',
    devtool: 'source-map',
    output: {
        path: path.resolve('./public/bundles/js'),
        filename: '[name].[hash].js'
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
        new CleanWebpackPlugin(),
        new MiniCssExtractPlugin({
            filename: isDevelopment ? '../css/[name].css' : '../css/[name].[hash].css',
            chunkFilename: isDevelopment ? '../css/[id].css' : '../css/[id].[hash].css'
        })
    ],
    resolve: {
        extensions: ['.js', '.jsx', '.scss']
    }
}