using Newtonsoft.Json;
using System.Text;

#region   TelegramMessageModel
TelegramMessageModel msg = new TelegramMessageModel(
  chatId: 5522471500,
  firstName: "NICK",
  messageText: "Привет! Я POST запросом был",
  updateId: 12345,
  replyToMessageId: 30
  );

#endregion

ReplayMessageModel model = new ReplayMessageModel(msg);
string json = JsonConvert.SerializeObject(model);
//System.Console.WriteLine(json);

HttpClient hc = new HttpClient();





StringBuilder sb = new StringBuilder()
.Append("{ \"chat_id\": 5522471500,")
.Append("\"text\": \"Привет! Я POST запросом был\",")
.Append("\"reply_to_message_id\": 30,")
.Append(" \"reply_markup\":{\"keyboard\":")
.Append("[ [\"Раз123\"],[\"Три213\",\"Два312\"] ]")
.Append(" } }");

StringContent content = new StringContent(
  content: sb.ToString(),
  encoding: Encoding.UTF8,
  mediaType: "application/json"
);

var res = hc.PostAsync("https://api.telegram.org/bot5921413168:AAEAj0G0uDFldBdPTumjcY_TlgaKvnCVf58/sendMessage", content).Result;
System.Console.WriteLine(res);