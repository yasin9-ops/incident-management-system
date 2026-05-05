import { useState, useEffect } from "react";
import API from "../api";

function IncidentDetail({ incident }) {
    const [signals, setSignals] = useState([]);

    useEffect(() => {
        let intervalId;

        const fetchSignals = () => {
            if (incident) {
                API.get(`/incident/${incident.component_id}/signals`)
                    .then(res => setSignals(res.data))
                    .catch(err => console.error(err));
            }
        };

        fetchSignals(); // Initial fetch

        if (incident) {
            intervalId = setInterval(fetchSignals, 3000);
        }

        return () => {
            if (intervalId) clearInterval(intervalId);
        };
    }, [incident]);

    if (!incident) return <div>Select an incident</div>;

    return (
        <div style={{ marginBottom: "20px", padding: "10px", border: "1px solid #ccc" }}>
            <h3>{incident.component_id}</h3>
            <p>Status: {incident.status}</p>

            {incident.mttr_seconds && (
                <p>MTTR: {incident.mttr_seconds} seconds</p>
            )}

            <h4>Raw Signals</h4>
            <div style={{ maxHeight: "200px", overflowY: "scroll", backgroundColor: "#f9f9f9", padding: "10px" }}>
                {signals.length === 0 ? <p>No raw signals found.</p> : (
                    <ul>
                        {signals.map((sig, i) => (
                            <li key={i}>
                                <strong>{sig.severity}</strong>: {sig.message} <em>({sig.timestamp})</em>
                            </li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
}

export default IncidentDetail;