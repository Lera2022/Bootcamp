using Microsoft.EntityFrameworkCore;

public class StorageContext : DbContext
{
  string dbName;
  public StorageContext(string dbName)
  {
    this.dbName = dbName;
  }
  public DbSet<Worker> Workers_t { get; set; }

  protected override void OnConfiguring(
    DbContextOptionsBuilder optionsBuilder)
  {
    string connectionString =
    @"Host={0}; Username={1}; Password={2};Database={3}";
    optionsBuilder.UseNpgsql(
     String.Format(connectionString,
     "localhost:5432",
     "i",
     "1111",
     dbName
     ));
  }
}
