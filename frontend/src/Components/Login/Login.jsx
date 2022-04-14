import React, { useState } from "react";
import axios from "axios";
import { Formik, Field, Form, ErrorMessage } from "formik";

import "./Login.css";

function Login() {
  const [inputs, setInputs] = useState({
    username: "",
    password: "",
  });

  const [accessToken, setAccessToken] = useState("");
  const [refreshToken, setRefreshToken] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        `http://www.localhost:8000/users/login`,
        inputs
      );
      setAccessToken(res.data.access_token);
      setRefreshToken(res.data.refresh_token);
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

  const fetchUsersData = async (e) => {
    try {
      const res = await axios.get("http://localhost:8000/users/user", {
        headers: {
          authorization: `Bearer ${accessToken}`,
        },
      });
      console.log(res);
    } catch (err) {
      console.log(err.response);
      if (err.response.status == 422) {
        try {
          const res = await axios.post(
            "http://www.localhost:8000/users/refresh",
            {},
            { headers: { Authorization: `Bearer ${refreshToken}` } }
          );
          console.log(res.data);
          setAccessToken(res.data.access_token);
        } catch (err) {
          console.log(err.response);
        }
      }
    }
  };

  const getRefreshToken = async (e) => {
    try {
      const res = await axios.post("http://localhost:8000/users/refresh", {
        headers: {
          authorization: `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkZXZlbjEyMzQ1IiwiaWF0IjoxNjQ5OTE5NDA4LCJuYmYiOjE2NDk5MTk0MDgsImp0aSI6ImZhODNhYWJmLTM1OWQtNDZhNC1iNmFlLTU1ODE2MTk4NzBjZiIsImV4cCI6MTY1MjUxMTQwOCwidHlwZSI6InJlZnJlc2gifQ.jLLPJfqSqWhISNoi-Zpm4OyJdUi5PWtNRIUb10X7fj0`,
        },
      });
      console.log(res.data);
    } catch (err) {
      console.log(err.response);
    }
  };

  return (
    <div className="login">
      <div className="login-component">
        <h3>Loginn</h3>
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
        <br />
        <br />
        <button onClick={fetchUsersData}>Fetch Data</button>
        <br />
        <br />
        <button onClick={getRefreshToken}>Get access token</button>
      </div>
    </div>
  );
}

export default Login;
