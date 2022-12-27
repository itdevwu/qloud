import React from 'react';
import { Button, InputNumber, Form } from 'antd';
import axios from 'axios';

const App = () => {
    const onFinish = (values) => {
        axios.post('http://127.0.0.1:8000/createjob', {
            "number": values.number,
            "experiment_iter": values.experiment_iter
        })
            .then(function (response) {
                console.log(response.data.msg);
                window.location.pathname = "/job/" + response.data.msg;
            })
            .catch(function (error) {
                console.log(error);
            });
        console.log('Success:', values);
    };
    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };
    return (
        <Form
            name="grover"
            labelAlign="right"
            labelCol={{
                offset: 2,
                span: 8,
            }}
            wrapperCol={{
                offset: 0,
                span: 12,
            }}
            onFinish={onFinish}
            onFinishFailed={onFinishFailed}
            autoComplete="off"
        >
            <Form.Item
                label={<label style={{ color: "#fff" }}>目标整数</label>}
                name="number"
                rules={[
                    {
                        required: true,
                        message: '请输入要分解的正整数',
                    },
                ]}
            >
                <InputNumber min={1} />
            </Form.Item>

            <Form.Item
                label={<label style={{ color: "#fff" }}>实验次数</label>}
                name="experiment_iter"
                rules={[
                    {
                        required: true,
                        message: '请输入实验次数',
                    },
                ]}
            >
                <InputNumber min={1} />
            </Form.Item>

            <Form.Item
                wrapperCol={{
                    offset: 0,
                    span: 24,
                }}
            >
                <Button color='#fff' ghost="true" htmlType="submit">
                    开始模拟
                </Button>
            </Form.Item>
        </Form>
    );
};
export default App;