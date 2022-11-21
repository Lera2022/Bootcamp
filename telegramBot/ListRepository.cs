

public class ListRepository : IRepository<Worker>
{
  List<Worker> list = new List<Worker>();
  int index = 0;

  public void Create(Worker item)
  {
    index++;
    item.Id = index;
    list.Add(item);
  }

  public void Delete(int id)
  {
    list.RemoveAll(e => e.Id == id);
  }

  public Worker[] Read()
  {
    return list.ToArray();
  }

  public void Update(int id, Worker newItem)
  {
    var index = list.Find(e => e.Id == id).Id - 1;
    list[index] = newItem;
    list[index].Id = id;
  }
}
