package services;

import entities.Machine;
import entities.Salle;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.List;

public class MachineServiceTest {

    private MachineService machineService;
    private SalleService salleService;

    @BeforeEach
    public void setUp() {
        machineService = new MachineService();
        salleService = new SalleService();
    }

    @Test
    public void testCreateMachineWithSalle() {
        Salle salle = new Salle("T1", "Salle Test Machines");
        salleService.create(salle);

        Machine m = new Machine("MAC-01", "Apple", salle);
        boolean created = machineService.create(m);
        Assertions.assertTrue(created, "La creation de la machine avec salle associee doit reussir");
        Assertions.assertTrue(m.getId() > 0, "L'id genere de la machine doit etre positif");
    }

    @Test
    public void testFindByMarqueHql() {
        Salle salle = new Salle("T2", "Salle Laboratoire");
        salleService.create(salle);

        Machine m1 = new Machine("LEN-01", "Lenovo", salle);
        Machine m2 = new Machine("LEN-02", "Lenovo", salle);
        machineService.create(m1);
        machineService.create(m2);

        List<Machine> lenovos = machineService.findByMarque("Lenovo");
        Assertions.assertNotNull(lenovos, "La liste de resultat HQL ne doit pas etre nulle");
        Assertions.assertTrue(lenovos.size() >= 2, "La requete HQL findByMarque doit retourner au moins 2 machines Lenovo");
    }

    @Test
    public void testUpdateAndDeleteMachine() {
        Salle salle = new Salle("T3", "Salle Maintenance");
        salleService.create(salle);

        Machine m = new Machine("ASUS-01", "Asus", salle);
        machineService.create(m);

        m.setMarque("Asus ROG");
        boolean updated = machineService.update(m);
        Assertions.assertTrue(updated, "La mise a jour de la machine doit reussir");

        boolean deleted = machineService.delete(m);
        Assertions.assertTrue(deleted, "La suppression de la machine doit reussir");
    }
}
