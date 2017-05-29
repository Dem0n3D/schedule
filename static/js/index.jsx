import $ from 'jquery';

import _ from 'underscore';
import classNames from 'classnames';

import axios from 'axios';

import React from 'react';
import ReactDOM from 'react-dom';
import {createStore, combineReducers, applyMiddleware} from 'redux';
import {Provider, connect} from 'react-redux';
import thunkMiddleware from 'redux-thunk';

import {GroupList} from './group';
import {CorpusList} from './corpus';

import '../css/style.css';


const reducer = combineReducers({
});

const store = createStore(reducer, applyMiddleware(thunkMiddleware));


class App extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            groups: [],
            corpus: [],
        };
    }

    componentDidMount() {
        axios.get("/api/v1/group").then(r => this.setState({groups: r.data}));
        axios.get("/api/v1/corpus").then(r => this.setState({corpus: r.data}));
    }

    render() {
        return (
            <div>
                <h1>Scheduler</h1>

                <GroupList data={this.state.groups} />
                <CorpusList data={this.state.corpus} />
            </div>
        );
    }

}

$(function() {
    ReactDOM.render(
        <Provider store={store}>
            <App/>
        </Provider>,
        $("#app")[0]
    );
});
