import React from 'react';
import './index.css';
import logo from './quantum.svg'
import 'antd/dist/reset.css';
import App from './App';
import { Link } from "react-router-dom";

export default function Main() {
    return (
        <>
            <div id='main'>
                <div id='logo'>
                    <Link to={"/"}>
                        <img src={logo} className="App-logo" alt="logo" />
                    </Link>
                    <h1 id='logo-text'>Qloud</h1>
                </div>
                <div id='quote'>
                    <i>Grover 算法的仿真平台</i>
                </div>

                <div id='form'>
                    <App />
                </div>
            </div>
        </>
    );
}