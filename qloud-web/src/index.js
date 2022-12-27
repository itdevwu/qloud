import React from 'react';
import ReactDOM from 'react-dom/client';
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import './index.css';
import 'antd/dist/reset.css';
import Main from './main';
import Job from './Job';

const router = createBrowserRouter([
    {
        path: "/",
        element: <Main />,
    },
    {
        path: "job/:id",
        element: <Job />
    }
]);

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
);

