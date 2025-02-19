const updateTrack = (track) => {
    document.getElementById("current-track").innerText = track;
  };
  
  document.getElementById("pause-btn").addEventListener("click", () => {
    fetch("/api/player", {
      method: "POST",
      body: JSON.stringify({ action: "pause" }),
      headers: { "Content-Type": "application/json" }
    });
  });
  
  document.getElementById("next-btn").addEventListener("click", () => {
    fetch("/api/player", {
      method: "POST",
      body: JSON.stringify({ action: "play", track: "New Track" }),
      headers: { "Content-Type": "application/json" }
    });
  });
  