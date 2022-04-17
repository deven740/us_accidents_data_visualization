import React, { useState } from "react";
import axiosApiInstance from "../../AxiosInstancs.js";
import { toast } from "react-toastify";
import axios from "axios";

import "./Login.css";

function Login() {
  const [inputs, setInputs] = useState({
    username: "",
    password: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        `http://www.localhost:8000/users/login`,
        inputs
      );
      localStorage.setItem("access_token", res.data.access_token);
      localStorage.setItem("refresh_token", res.data.refresh_token);
      toast.success("Logged in Sucessfully");
    } catch (err) {
      toast.error(err.response.data.detail);
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
      const res = await axiosApiInstance.get(
        "http://localhost:8000/users/user"
      );
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
      </div>
    </div>
  );
}

export default Login;
