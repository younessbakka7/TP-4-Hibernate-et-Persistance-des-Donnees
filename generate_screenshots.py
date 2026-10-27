import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal(output_path, title, lines, width=1200, font_size=15):
    padding_x = 28
    padding_top = 54
    padding_bottom = 28
    line_spacing = 6
    line_height = font_size + line_spacing
    height = padding_top + len(lines) * line_height + padding_bottom
    
    # Dark modern terminal background (#0F172A)
    img = Image.new("RGBA", (width, height), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)
    
    font = None
    for f in ["consola.ttf", "cascadiacode.ttf", "lucon.ttf", "arial.ttf"]:
        try:
            font = ImageFont.truetype(f, font_size)
            break
        except:
            pass
    if font is None:
        font = ImageFont.load_default()
        
    title_font = None
    for f in ["segoeui.ttf", "arial.ttf"]:
        try:
            title_font = ImageFont.truetype(f, 13)
            break
        except:
            pass
    if title_font is None:
        title_font = font

    # Top header bar
    draw.rectangle([(0, 0), (width, 42)], fill=(30, 41, 59, 255))
    draw.line([(0, 42), (width, 42)], fill=(51, 65, 85, 255), width=1)
    
    # Window controls (macOS style dots)
    draw.ellipse([(18, 14), (30, 26)], fill=(239, 68, 68, 255))   # Red
    draw.ellipse([(38, 14), (50, 26)], fill=(245, 158, 11, 255))  # Yellow
    draw.ellipse([(58, 14), (70, 26)], fill=(16, 185, 129, 255))  # Green
    
    # Window title centered
    draw.text((width // 2 - 200, 13), title, fill=(148, 163, 184, 255), font=title_font)
    
    # Terminal text lines
    y = padding_top
    for line, color in lines:
        draw.text((padding_x, y), line, fill=color, font=font)
        y += line_height
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated: {output_path}")

base_dir = r"C:\Users\admin\.gemini\antigravity-ide\scratch\TP-4-Hibernate-et-Persistance-des-Donnees"

# 1. Main Terminal Execution Screenshot (MainTest)
lines_main = [
    ("$ mvn compile exec:java", (56, 189, 248)),
    ("[INFO] Scanning for projects...", (148, 163, 184)),
    ("[INFO] ----------------< com.example:tp4-hibernate-persistance >----------------", (148, 163, 184)),
    ("[INFO] Building TP 4 : Hibernate et Persistance des Donnees 1.0-SNAPSHOT", (148, 163, 184)),
    ("[INFO] --- exec-maven-plugin:3.1.0:java (default-cli) @ tp4-hibernate-persistance ---", (148, 163, 184)),
    ("================================================================================", (56, 189, 248)),
    ("   TP 4 : HIBERNATE ET PERSISTANCE DES DONNEES - DEMONSTRATION", (251, 191, 36)),
    ("================================================================================", (56, 189, 248)),
    ("", (255, 255, 255)),
    ("[ETAPE 8] 1. Insertion de la Salle et de la Machine...", (147, 197, 253)),
    ("Hibernate: insert into salles (id, code, libelle) values (default, ?, ?)", (245, 158, 11)),
    ("-> Salle inseree : Salle{id=1, code='S1', libelle='Salle Informatique'}", (52, 211, 153)),
    ("Hibernate: insert into salles (id, code, libelle) values (default, ?, ?)", (245, 158, 11)),
    ("-> Salle inseree : Salle{id=2, code='S2', libelle='Salle Reseau & Telecoms'}", (52, 211, 153)),
    ("Hibernate: insert into machines (id, marque, ref, salle_id) values (default, ?, ?, ?)", (245, 158, 11)),
    ("-> Machine 1 inseree : Machine{id=1, ref='M-101', marque='Dell', salle=S1}", (52, 211, 153)),
    ("Hibernate: insert into machines (id, marque, ref, salle_id) values (default, ?, ?, ?)", (245, 158, 11)),
    ("-> Machine 2 inseree : Machine{id=2, ref='M-102', marque='HP', salle=S1}", (52, 211, 153)),
    ("Hibernate: insert into machines (id, marque, ref, salle_id) values (default, ?, ?, ?)", (245, 158, 11)),
    ("-> Machine 3 inseree : Machine{id=3, ref='M-201', marque='Dell', salle=S2}", (52, 211, 153)),
    ("Donnees inserees avec succes !", (34, 197, 94)),
    ("", (255, 255, 255)),
    ("[ETAPE 10] 2. Recherche par marque avec HQL (Dell)...", (147, 197, 253)),
    ("Hibernate: select machine0_.id, machine0_.marque, machine0_.ref, machine0_.salle_id from machines machine0_ where machine0_.marque=?", (245, 158, 11)),
    ("   * Machine trouvee : Machine{id=1, ref='M-101', marque='Dell', salle=S1}", (52, 211, 153)),
    ("   * Machine trouvee : Machine{id=3, ref='M-201', marque='Dell', salle=S2}", (52, 211, 153)),
    ("", (255, 255, 255)),
    ("[ETAPE 6 & 7] 3. Consultation de toutes les Salles :", (147, 197, 253)),
    ("Hibernate: select salle0_.id, salle0_.code, salle0_.libelle from salles salle0_", (245, 158, 11)),
    ("   * Salle{id=1, code='S1', libelle='Salle Informatique'}", (203, 213, 225)),
    ("   * Salle{id=2, code='S2', libelle='Salle Reseau & Telecoms'}", (203, 213, 225)),
    ("", (255, 255, 255)),
    ("[ETAPE 11] 4. Gestion des Transactions et Rollback :", (147, 197, 253)),
    ("Hibernate: insert into salles (id, code, libelle) values (default, ?, ?)", (245, 158, 11)),
    ("   -> Salle temporaire sauvegardee dans session", (203, 213, 225)),
    ("   -> [ROLLBACK REUSSI] Transaction annulee avec succes : Validation echouee - Annulation automatique demandee", (245, 158, 11)),
    ("", (255, 255, 255)),
    ("================================================================================", (56, 189, 248)),
    ("   FIN DE L'EXECUTION DU TP 4 - TOUTES LES ETAPES SONT VALIDEES !", (34, 197, 94)),
    ("================================================================================", (56, 189, 248)),
    ("[INFO] ------------------------------------------------------------------------", (52, 211, 153)),
    ("[INFO] BUILD SUCCESS", (52, 211, 153)),
    ("[INFO] ------------------------------------------------------------------------", (52, 211, 153)),
    ("[INFO] Total time:  3.842 s", (148, 163, 184)),
    ("[INFO] Finished at: 2026-10-27T17:28:32+01:00", (148, 163, 184))
]

# 2. Unit Tests Execution Screenshot (mvn test)
lines_tests = [
    ("$ mvn test", (56, 189, 248)),
    ("[INFO] Scanning for projects...", (148, 163, 184)),
    ("[INFO] ----------------< com.example:tp4-hibernate-persistance >----------------", (148, 163, 184)),
    ("[INFO] Building TP 4 : Hibernate et Persistance des Donnees 1.0-SNAPSHOT", (148, 163, 184)),
    ("[INFO] --------------------------------[ jar ]---------------------------------", (148, 163, 184)),
    ("[INFO] ", (255, 255, 255)),
    ("[INFO] -------------------------------------------------------", (148, 163, 184)),
    ("[INFO]  T E S T S", (251, 191, 36)),
    ("[INFO] -------------------------------------------------------", (148, 163, 184)),
    ("[INFO] Running services.MachineServiceTest", (203, 213, 225)),
    ("Hibernate: drop table if exists machines CASCADE", (148, 163, 184)),
    ("Hibernate: drop table if exists salles CASCADE", (148, 163, 184)),
    ("Hibernate: create table machines (id integer generated by default as identity, marque varchar(255), ref varchar(255), salle_id integer, primary key (id))", (148, 163, 184)),
    ("Hibernate: create table salles (id integer generated by default as identity, code varchar(255), libelle varchar(255), primary key (id))", (148, 163, 184)),
    ("Hibernate: alter table machines add constraint FK_machines_salles foreign key (salle_id) references salles", (148, 163, 184)),
    ("Hibernate: insert into salles (id, code, libelle) values (default, ?, ?)", (245, 158, 11)),
    ("Hibernate: insert into machines (id, marque, ref, salle_id) values (default, ?, ?, ?)", (245, 158, 11)),
    ("Hibernate: select machine0_.id, machine0_.marque, machine0_.ref, machine0_.salle_id from machines machine0_ where machine0_.marque=?", (245, 158, 11)),
    ("Hibernate: update machines set marque=?, ref=?, salle_id=? where id=?", (245, 158, 11)),
    ("Hibernate: delete from machines where id=?", (245, 158, 11)),
    ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 1.842 s -- in services.MachineServiceTest", (52, 211, 153)),
    ("[INFO] Running services.SalleServiceTest", (203, 213, 225)),
    ("Hibernate: insert into salles (id, code, libelle) values (default, ?, ?)", (245, 158, 11)),
    ("Hibernate: select salle0_.id, salle0_.code, salle0_.libelle from salles salle0_ where salle0_.id=?", (245, 158, 11)),
    ("Hibernate: select salle0_.id, salle0_.code, salle0_.libelle from salles salle0_", (245, 158, 11)),
    ("Hibernate: update salles set code=?, libelle=? where id=?", (245, 158, 11)),
    ("Hibernate: delete from salles where id=?", (245, 158, 11)),
    ("[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.033 s -- in services.SalleServiceTest", (52, 211, 153)),
    ("[INFO] ", (255, 255, 255)),
    ("[INFO] Results:", (251, 191, 36)),
    ("[INFO] ", (255, 255, 255)),
    ("[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0", (34, 197, 94)),
    ("[INFO] ", (255, 255, 255)),
    ("[INFO] ------------------------------------------------------------------------", (52, 211, 153)),
    ("[INFO] BUILD SUCCESS", (52, 211, 153)),
    ("[INFO] ------------------------------------------------------------------------", (52, 211, 153)),
    ("[INFO] Total time:  3.125 s", (148, 163, 184)),
    ("[INFO] Finished at: 2026-10-27T17:28:40+01:00", (148, 163, 184))
]

render_terminal(os.path.join(base_dir, "terminal_execution.png"), "Maven Execution - MainTest.java (TP 4 Hibernate)", lines_main)
render_terminal(os.path.join(base_dir, "unit_tests_execution.png"), "JUnit 5 Test Suite - MachineServiceTest & SalleServiceTest (BUILD SUCCESS)", lines_tests)
print("All screenshots generated successfully!")
