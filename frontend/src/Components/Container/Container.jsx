import React from "react";
import "./Container.css";
import SideBar from "../SideBar/SideBar";
import MainPage from "../MainPage/MainPage";

function Container() {
  return (
    <div className="container">
      <SideBar />
      <MainPage />
    </div>
  );
}

export default Container;
