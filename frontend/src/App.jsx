import { useEffect, useState } from "react";
import axios from "axios";

export default function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchEvents = async () => {
    try {
      const res = await axios.get("http://localhost:5000/events");

      const unique = Array.from(
        new Map(res.data.map((e) => [e.request_id, e])).values()
      );

      setEvents(unique);
      setLoading(false);
    } catch (err) {
      console.error("❌ Error fetching:", err);
    }
  };

  useEffect(() => {
    fetchEvents();
    const interval = setInterval(fetchEvents, 15000);
    return () => clearInterval(interval);
  }, []);

  const formatMessage = (e) => {
    if (e.action === "PUSH") {
      return `${e.author} pushed to ${e.to_branch} on ${e.timestamp}`;
    }
    if (e.action === "PULL_REQUEST") {
      return `${e.author} submitted a pull request from ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
    }
    if (e.action === "MERGE") {
      return `${e.author} merged branch ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
    }
  };

  const getBadgeColor = (action) => {
    if (action === "PUSH") return "#3b82f6";
    if (action === "PULL_REQUEST") return "#f59e0b";
    if (action === "MERGE") return "#10b981";
  };

  return (
    <div style={{ padding: "30px", background: "#f3f4f6", minHeight: "100vh" }}>
      
      <h1 style={{ fontSize: "28px", marginBottom: "20px" }}>
        🚀 GitHub Activity Dashboard
      </h1>

      {loading ? (
        <p>Loading events...</p>
      ) : events.length === 0 ? (
        <p>No activity yet...</p>
      ) : (
        events.map((e) => (
          <div
            key={e._id}
            style={{
              background: "#fff",
              padding: "15px",
              marginBottom: "12px",
              borderRadius: "10px",
              boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div>
              <p style={{ margin: 0, fontWeight: "500" }}>
                {formatMessage(e)}
              </p>
            </div>

            <span
              style={{
                background: getBadgeColor(e.action),
                color: "#fff",
                padding: "5px 10px",
                borderRadius: "20px",
                fontSize: "12px",
              }}
            >
              {e.action}
            </span>
          </div>
        ))
      )}
    </div>
  );
}