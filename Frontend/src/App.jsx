import { useState } from "react";
import IncidentList from "./components/IncidentList";
import IncidentDetail from "./components/IncidentDetail";
import RCAForm from "./components/RCAForm";

function App() {
  const [selectedIncident, setSelectedIncident] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚨 Incident Management System</h1>

      <div style={{ display: "flex", gap: "20px" }}>
        {/* LEFT SIDE - Incident List */}
        <div style={{ width: "30%" }}>
          <IncidentList onSelect={setSelectedIncident} />
        </div>

        {/* RIGHT SIDE - Details + RCA */}
        <div style={{ width: "70%" }}>
          <IncidentDetail incident={selectedIncident} />
          <RCAForm incident={selectedIncident} />
        </div>
      </div>
    </div>
  );
}

export default App;