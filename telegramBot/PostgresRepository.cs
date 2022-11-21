using Microsoft.EntityFrameworkCore;

public class PostgresRepository : IRepository<Worker>
{
  StorageContext db;



  public PostgresRepository(string dbName)
  {
    db = new StorageContext(dbName);
    db.Database.EnsureDeleted();
    db.Database.EnsureCreated();
  }

  public void Create(Worker item)
  {
    db.Workers_t.Add(item);
    db.SaveChanges();
  }

  public void Delete(int id)
  {
    Worker t = db.Workers_t.First(e => e.Id == id);
    db.Entry(t).State = EntityState.Deleted;
    db.SaveChanges();
  }

  public Worker[] Read()
  {
    return db.Workers_t.ToArray();
  }

  public void Update(int id, Worker newItem)
  {
    Worker t = db.Workers_t.First(e => e.Id == id);
    t.Age = newItem.Age;
    t.Salary = newItem.Salary;
    t.FullName = newItem.FullName;
    db.Entry(t).State = EntityState.Modified;
    db.SaveChanges();
  }
}
