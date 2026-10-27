package services;

import entities.Salle;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.List;

public class SalleServiceTest {

    private SalleService service;

    @BeforeEach
    public void setUp() {
        service = new SalleService();
    }

    @Test
    public void testCreateSalle() {
        Salle salle = new Salle();
        salle.setCode("S2");
        salle.setLibelle("Salle Reseau");

        boolean result = service.create(salle);
        Assertions.assertTrue(result, "La creation de la salle doit reussir");
        Assertions.assertTrue(salle.getId() > 0, "L'identifiant auto-genere doit etre strictement positif");
    }

    @Test
    public void testGetByIdAndGetAll() {
        Salle salle = new Salle("S3", "Salle Multimedia");
        service.create(salle);

        Salle found = service.getById(salle.getId());
        Assertions.assertNotNull(found, "La salle recherchee par id doit exister");
        Assertions.assertEquals("S3", found.getCode());

        List<Salle> all = service.getAll();
        Assertions.assertFalse(all.isEmpty(), "La liste des salles ne doit pas etre vide");
    }

    @Test
    public void testUpdateAndDelete() {
        Salle salle = new Salle("S4", "Salle Conference");
        service.create(salle);

        salle.setLibelle("Salle Conference Renovee");
        boolean updated = service.update(salle);
        Assertions.assertTrue(updated, "La mise a jour de la salle doit reussir");

        boolean deleted = service.delete(salle);
        Assertions.assertTrue(deleted, "La suppression de la salle doit reussir");
    }
}
