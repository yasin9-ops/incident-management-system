import { useState } from "react";
import API from "../api";

function RCAForm({ incident }) {
  const [rootCause, setRootCause] = useState("");
  const [fix, setFix] = useState("");
  const [prevention, setPrevention] = useState("");
  const [startTime, setStartTime] = useState("");
  const [endTime, setEndTime] = useState("");

  const submitRCA = () => {
    API.post(`/incident/${incident.component_id}/status?status=CLOSED`, {
      root_cause: rootCause,
      fix: fix,
      prevention: prevention
    }).then(res => {
        if(res.data.error) {
            alert("Error: " + res.data.error);
        } else {
            alert(`Incident closed! MTTR: ${res.data.mttr_seconds} seconds`);
        }
    });
  };

  if (!incident) return null;

  return (
    <div style={{ padding: "10px", border: "1px solid #ccc" }}>
      <h3>RCA Form</h3>
      <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
          <div>
              <label>Incident Start Time: </label>
              <input type="datetime-local" value={startTime} onChange={(e) => setStartTime(e.target.value)} />
          </div>
          <div>
              <label>Incident End Time: </label>
              <input type="datetime-local" value={endTime} onChange={(e) => setEndTime(e.target.value)} />
          </div>

          <select value={rootCause} onChange={(e) => setRootCause(e.target.value)}>
              <option value="">-- Select Root Cause Category --</option>
              <option value="Code Bug">Code Bug</option>
              <option value="Infrastructure Failure">Infrastructure Failure</option>
              <option value="Network Outage">Network Outage</option>
              <option value="Third-Party API">Third-Party API Down</option>
          </select>
          
          <textarea
            placeholder="Fix Applied"
            rows={4}
            value={fix}
            onChange={(e) => setFix(e.target.value)}
          />
          <textarea
            placeholder="Prevention Steps"
            rows={4}
            value={prevention}
            onChange={(e) => setPrevention(e.target.value)}
          />
          <button onClick={submitRCA} style={{ padding: "10px", backgroundColor: "#007bff", color: "#fff", border: "none", cursor: "pointer" }}>
            Submit RCA & Close Incident
          </button>
      </div>
    </div>
  );
}

export default RCAForm;