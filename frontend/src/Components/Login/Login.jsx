import React from "react";
import axios from "axios";
import { Formik, Field, Form, ErrorMessage } from "formik";

import "./Login.css";

function Login() {
  return (
    <div className="login">
      <div className="login-component">
        <Formik
          initialValues={{ username: "", password: "" }}
          validate={(values) => {
            const errors = {};
            if (values.username.length < 8) {
              errors.username = "Username cannot be less than 8 characters";
            }
            if (values.password.length < 8) {
              errors.password = "Password cannot be less than 8 characters";
            }
            return errors;
          }}
          onSubmit={async (values) => {
            console.log(values);
            const data = {
              username: "deven12345",
              password: "deven12345",
            };
            await axios.post(`http://www.localhost:8000/users/login`, data);
            // await axios.get("http://127.0.0.1:8000/users/").then((res) => {
            //   console.log(res);
            //   console.log(res.data);
            // });
          }}
        >
          <Form className="login-form">
            <Field name="username" type="text" />
            <ErrorMessage name="username" component="div" />
            <Field name="password" type="password" />
            <ErrorMessage name="password" component="div" />
            <button type="submit">Submit</button>
          </Form>
        </Formik>
      </div>
    </div>
  );
}

export default Login;
