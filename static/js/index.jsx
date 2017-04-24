import $ from 'jquery';

import _ from 'underscore';
import classNames from 'classnames';

import React from 'react';
import ReactDOM from 'react-dom';
import {createStore, combineReducers, applyMiddleware} from 'redux';
import {Provider, connect} from 'react-redux';
import thunkMiddleware from 'redux-thunk';

const reducer = combineReducers({
});
const store = createStore(reducer, applyMiddleware(thunkMiddleware));

$(function() {
    ReactDOM.render(
        <Provider store={store}>
        </Provider>,
        $("#app")[0]
    );
});
