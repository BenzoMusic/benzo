module.exports = async (req, res) => {
    const { body } = req;
    console.log("Received update:", body);
  
    // Обработка команд от Telegram
    if (body.message) {
      const { text, chat } = body.message;
      if (text === "/start") {
        res.json({ method: "sendMessage", chat_id: chat.id, text: "Привет! Отправь ссылку на трек." });
      }
    }
  
    res.status(200).end();
  };
  