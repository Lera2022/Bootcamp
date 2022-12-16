public class TelegramBot
{
  string token;
  public Action<TelegramMessageModel> action;
  HttpClient hc;
  Thread thread;

  public TelegramBot(string token)
  {
    this.token = token;
    hc = new HttpClient();
    hc.BaseAddress = new Uri($"http://api.telegram.org/bot{token}/");
    thread = new Thread(GetUpdates);
  }

  private void GetUpdates()
  {
    long offset = 0;
    while (true)
    {
      string content = hc.GetStringAsync($"getupdates?offset={offset + 1}").Result;
      try
      {
        TelegramMessageModel[] ms = new JsonParser().GetMessage(content);
        if (ms.Length != 0)
        {
          foreach (var item in ms)
          {
            Console.WriteLine(item);
            action(item);
            offset = item.updateId;
          }
        }
      }
      catch
      {
        Console.WriteLine("ОШИБКА !!!");
      }
      Thread.Sleep(1000);
    }

  }

  public void SendMessage(long userId, string text)
  {
    ..НАДО РЕАЛИЗОВАТЬ
  }

  public void Start()
  {
    thread.Start();
  }
}