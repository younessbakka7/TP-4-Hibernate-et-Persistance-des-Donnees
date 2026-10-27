package dao;

import java.util.List;

/**
 * Interface générique DAO définissant les opérations CRUD standards.
 * @param <T> Type de l'entité
 */
public interface IDao<T> {
    boolean create(T o);
    boolean delete(T o);
    boolean update(T o);
    T getById(int id);
    List<T> getAll();
}
