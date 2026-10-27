package test;

import entities.Machine;
import entities.Salle;
import org.hibernate.Session;
import org.hibernate.Transaction;
import services.MachineService;
import services.SalleService;
import util.HibernateUtil;
import java.util.List;

public class MainTest {
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println("   TP 4 : HIBERNATE ET PERSISTANCE DES DONNEES - DEMONSTRATION");
        System.out.println("================================================================================");

        SalleService salleService = new SalleService();
        MachineService machineService = new MachineService();

        System.out.println("\n[ETAPE 8] 1. Insertion de la Salle et de la Machine...");
        Salle salleA = new Salle();
        salleA.setCode("S1");
        salleA.setLibelle("Salle Informatique");
        salleService.create(salleA);
        System.out.println("-> Salle inseree : " + salleA);

        Salle salleB = new Salle();
        salleB.setCode("S2");
        salleB.setLibelle("Salle Reseau & Telecoms");
        salleService.create(salleB);
        System.out.println("-> Salle inseree : " + salleB);

        Machine machine1 = new Machine();
        machine1.setRef("M-101");
        machine1.setMarque("Dell");
        machine1.setSalle(salleA);
        machineService.create(machine1);
        System.out.println("-> Machine 1 inseree : " + machine1);

        Machine machine2 = new Machine();
        machine2.setRef("M-102");
        machine2.setMarque("HP");
        machine2.setSalle(salleA);
        machineService.create(machine2);
        System.out.println("-> Machine 2 inseree : " + machine2);

        Machine machine3 = new Machine();
        machine3.setRef("M-201");
        machine3.setMarque("Dell");
        machine3.setSalle(salleB);
        machineService.create(machine3);
        System.out.println("-> Machine 3 inseree : " + machine3);

        System.out.println("Donnees inserees avec succes !");

        System.out.println("\n[ETAPE 10] 2. Recherche par marque avec HQL (Dell)...");
        List<Machine> dellMachines = machineService.findByMarque("Dell");
        for (Machine m : dellMachines) {
            System.out.println("   * Machine trouvee : " + m);
        }

        System.out.println("\n[ETAPE 6 & 7] 3. Consultation de toutes les Salles :");
        List<Salle> salles = salleService.getAll();
        for (Salle s : salles) {
            System.out.println("   * " + s);
        }

        System.out.println("\n[ETAPE 11] 4. Gestion des Transactions et Rollback :");
        Session session = null;
        Transaction tx = null;
        try {
            session = HibernateUtil.getSessionFactory().openSession();
            tx = session.beginTransaction();
            Salle salleTemp = new Salle("TEMP", "Salle Temporaire Test Rollback");
            session.save(salleTemp);
            System.out.println("   -> Salle temporaire sauvegardee dans session");
            boolean erreurVolontaire = true;
            if (erreurVolontaire) {
                throw new RuntimeException("Validation echouee - Annulation automatique demandee");
            }
            tx.commit();
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            System.out.println("   -> [ROLLBACK REUSSI] Transaction annulee avec succes : " + e.getMessage());
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
        }

        System.out.println("\n================================================================================");
        System.out.println("   FIN DE L'EXECUTION DU TP 4 - TOUTES LES ETAPES SONT VALIDEES !");
        System.out.println("================================================================================");

        HibernateUtil.getSessionFactory().close();
    }
}
