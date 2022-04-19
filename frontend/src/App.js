import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import "./App.css";
import Container from "./Components/Container/Container";
import Login from "./Components/Login/Login";
import Supervisor from "./Components/Supervisor/Supervisor";
import Admin from "./Components/Admin/Admin";

function App() {
  return (
    <div className="App">
      <ToastContainer />

      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Container />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/supervisor" element={<Supervisor />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
