import React, { Component } from 'react';
import './index.css';
import './Job.css'
import logo from './quantum.svg'
import 'antd/dist/reset.css';
import axios from 'axios';
import { Col, Row } from 'antd';
import withRouter from './withRouter';
import * as echarts from "echarts";
import { Link } from "react-router-dom";

class Job extends Component {
    constructor(props) {
        super(props);

        this.state = {
            job_num: -1,
            job_iter: -1,
            job_status: -1,
            job_res: {},
        };
    }

    componentDidMount() {
        let _this = this;
        axios.get('http://127.0.0.1:8000/job/' + this.props.params.id.toString())
            .then(function (response) {
                _this.setState({
                    job_num: response.data.job_num,
                    job_iter: response.data.job_iter,
                    job_status: response.data.job_status,
                    job_res: response.data.job_res,
                });

                var myChart = echarts.init(document.getElementById('chart'));
                // 显示标题，图例和空的坐标轴
                myChart.setOption({
                    title: {
                        text: '结果分布图'
                    },
                    tooltip: {},
                    legend: {
                        data: ['频率']
                    },
                    xAxis: {
                        data: []
                    },
                    yAxis: {},
                    series: [
                        {
                            name: '频率',
                            type: 'bar',
                            data: []
                        }
                    ]
                });
                myChart.setOption({
                    xAxis: {
                      data: response.data.x_axis
                    },
                    series: [
                      {
                        // 根据名字对应到相应的系列
                        name: '频率',
                        data: response.data.y_axis
                      }
                    ]
                  });
                console.log(response.data.x_axis);
                console.log(response.data.y_axis);


            })
            .catch(function (error) {
                console.log(error);
            });
    }

    render() {
        return <>
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

                <div id="experiment-info">
                    <Row>
                        <Col span={8}>目标整数</Col>
                        <Col span={8}>实验次数</Col>
                        <Col span={8}>实验状态</Col>
                    </Row>
                    <Row>
                        <Col span={8}>{this.state.job_num}</Col>
                        <Col span={8}>{this.state.job_iter}</Col>
                        <Col span={8}>{
                            this.state.job_status === 0 ? "等待中" : (
                                this.state.job_status === 1 ? "试验中" : "已完成"
                            )
                        }</Col>
                    </Row>
                </div>
                <div id="chart-block">
                    <Row>
                        <Col offset={8} span={8}>结果</Col>
                        <Col span={24}>
                            <div id="chart">
                            </div>
                        </Col>
                    </Row>
                </div>
            </div>
        </>
    };
}

export default withRouter(Job);
