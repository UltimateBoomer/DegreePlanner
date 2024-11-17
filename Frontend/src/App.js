import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import DegreePlanner from './Pages/DegreePlanner';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          {/* <Route path="/" element={<Home />} /> */}
          <Route path="/degree-planner" element={<DegreePlanner />} />
          {/* 404 Route
          <Route path="*" element={<NotFound />} /> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
