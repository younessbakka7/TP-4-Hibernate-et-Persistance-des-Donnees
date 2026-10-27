package util;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {
    private static final SessionFactory sessionFactory = buildSessionFactory();

    private static SessionFactory buildSessionFactory() {
        try {
            return new Configuration().configure().buildSessionFactory();
        } catch (Throwable ex) {
            System.err.println("Échec de la création de la SessionFactory standard : " + ex.getMessage());
            // Fallback transparent en mémoire H2 (mode MySQL) si MySQL local n'est pas démarré
            try {
                Configuration fallback = new Configuration();
                fallback.setProperty("hibernate.connection.driver_class", "org.h2.Driver");
                fallback.setProperty("hibernate.connection.url", "jdbc:h2:mem:db_tp_hibernate;MODE=MySQL;DATABASE_TO_LOWER=TRUE;DB_CLOSE_DELAY=-1");
                fallback.setProperty("hibernate.connection.username", "sa");
                fallback.setProperty("hibernate.connection.password", "");
                fallback.setProperty("hibernate.dialect", "org.hibernate.dialect.H2Dialect");
                fallback.setProperty("hibernate.hbm2ddl.auto", "create-drop");
                fallback.setProperty("hibernate.show_sql", "true");
                fallback.setProperty("hibernate.format_sql", "true");
                fallback.addAnnotatedClass(entities.Salle.class);
                fallback.addAnnotatedClass(entities.Machine.class);
                return fallback.buildSessionFactory();
            } catch (Throwable fallbackEx) {
                System.err.println("Échec du fallback SessionFactory : " + fallbackEx);
                throw new ExceptionInInitializerError(ex);
            }
        }
    }

    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }
}
