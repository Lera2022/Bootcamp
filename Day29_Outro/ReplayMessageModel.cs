// {
//   "updateId": 12345,
//   "chatId": 5522471500,
//   "text": "Привет! Я за тобой наблюдаю 2",
//   "firstName": "NICK",
//   "replyToMessageId": 30
// }

// {
//   "chat_id": 5522471500,
//   "text": "Привет! Я за тобой наблюдаю 2",
//   "reply_to_message_id": 30
// }

public class ReplayMessageModel
{
  public ReplayMessageModel(TelegramMessageModel model)
  {
    chat_id = model.chatId;
    text = model.text;
    reply_to_message_id = model.replyToMessageId;
  }
  public long chat_id { get; set; }
  public string text { get; set; }
  public long reply_to_message_id { get; set; }
}