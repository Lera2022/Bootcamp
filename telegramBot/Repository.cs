public interface IRepository<T>
{
  void Create(T item);
  T[] Read();
  void Update(int id, T newItem);
  void Delete(int Id);
}
