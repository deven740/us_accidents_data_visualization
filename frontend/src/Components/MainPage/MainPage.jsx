import React from "react";
import "./MainPage.css";

import NotificationsNoneIcon from "@mui/icons-material/NotificationsNone";
import MailOutlineIcon from "@mui/icons-material/MailOutline";
import Button from "@mui/material/Button";

function MainPage() {
  return (
    <div className="main-page">
      <div className="header-navbar">
        <div className="header-container">
          <div className="navbar-right">
            <div className="notifications">
              <NotificationsNoneIcon style={{ fontSize: 24 }} />
              <div className="notification-circle">3</div>
            </div>
            <div className="email">
              <MailOutlineIcon style={{ fontSize: 24 }} />
              <div className="notification-circle">3</div>
            </div>
            <div className="profile">
              <img
                src="https://randomuser.me/api/portraits/men/10.jpg"
                alt="profile"
                srcSet=""
              />
            </div>
            <div className="username">John Doe</div>
          </div>
          <div className="navbar-left"></div>
        </div>
      </div>
    </div>
  );
}

export default MainPage;
