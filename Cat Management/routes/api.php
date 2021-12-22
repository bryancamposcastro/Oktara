<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::get('/cats', 'App\Http\Controllers\CatController@index'); // Show all 
Route::post('/cats', 'App\Http\Controllers\CatController@store'); // Create 
Route::put('/cats/{id}', 'App\Http\Controllers\CatController@update'); // Update
Route::delete('/cats/{id}', 'App\Http\Controllers\CatController@destroy'); // Delete