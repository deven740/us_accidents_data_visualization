import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import "./App.css";
import Container from "./Components/Container/Container";
import Login from "./Components/Login/Login";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Container />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
