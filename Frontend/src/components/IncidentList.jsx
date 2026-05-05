import { useEffect, useState } from "react";
import API from "../api";

function IncidentList({ onSelect }) {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    const fetchIncidents = () => {
      API.get("/incidents")
        .then(res => setIncidents(res.data))
        .catch(err => console.error(err));
    };

    fetchIncidents(); // initial fetch
    const intervalId = setInterval(fetchIncidents, 3000); // Poll every 3 seconds

    return () => clearInterval(intervalId); // Cleanup
  }, []);

  return (
    <div>
      <h2>Incidents</h2>
      {incidents.length === 0 ? (
        <p>No incidents available.</p>
      ) : (
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {incidents.map((inc) => (
            <li
              key={inc.component_id}
              style={{
                border: "1px solid #ccc",
                padding: "10px",
                marginBottom: "10px",
                cursor: "pointer",
                backgroundColor: inc.status === "OPEN" ? "#ffebee" : "#f1f8e9"
              }}
              onClick={() => onSelect(inc)}
            >
              <strong>{inc.component_id}</strong>
              <br />
              Status: {inc.status} | Severity: {inc.severity}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default IncidentList;