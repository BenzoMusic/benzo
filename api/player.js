let currentTrack = null;

module.exports = async (req, res) => {
  const { action, track } = req.body;

  if (action === "play") {
    currentTrack = track;
  } else if (action === "pause") {
    currentTrack = null;
  }

  res.json({ status: "ok", track: currentTrack });
};
