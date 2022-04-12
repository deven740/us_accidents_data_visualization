import React, { useState } from "react";
import axios from "axios";
import { Formik, Field, Form, ErrorMessage } from "formik";

import "./Login.css";

function Login() {
  const [inputs, setInputs] = useState({
    username: "",
    password: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(inputs);
    // const data = {
    //   username: values.username,
    try {
      const res = await axios.post(
        `http://www.localhost:8000/users/login`,
        inputs
      );
      console.log(res);
    } catch (err) {
      console.log(err.response.data);
    }
  };

  const handleChange = (e) => {
    setInputs({
      ...inputs,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div className="login">
      <div className="login-component">
        <h3>Login</h3>
        <form action="post" className="login-form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="username"
            value={inputs.username}
            onChange={handleChange}
          />
          <input
            type="password"
            name="password"
            value={inputs.password}
            onChange={handleChange}
          />
          <input type="submit" value="Submit" />
        </form>
      </div>
    </div>
  );
}

export default Login;
