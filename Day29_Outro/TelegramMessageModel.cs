public class TelegramMessageModel
{
  public long updateId;
  public long chatId;
  public string text;
  public string firstName;
  public long replyToMessageId;

  public TelegramMessageModel(long chatId, string firstName, string messageText, long updateId, long replyToMessageId)
  {
    this.chatId = chatId;
    this.firstName = firstName;
    this.text = messageText;
    this.updateId = updateId;
    this.replyToMessageId = replyToMessageId;
  }

  public override string ToString()
  {
    return $"{firstName} {text} {chatId}  {updateId} ";
  }

}