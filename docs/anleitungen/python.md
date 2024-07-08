# Installation von Python

Hier ist eine einfache Schritt-für-Schritt-Anleitung zur Installation
von Python auf einem Windows 11-Rechner:

1. Öffnen Sie den Microsoft Store
   - Klicken Sie auf das Windows-Symbol unten links in der Taskleiste
   - Geben Sie "Microsoft Store" in die Suchleiste ein
   - Klicken Sie auf das Microsoft Store-Symbol, um den Store zu öffnen

2. Suchen Sie nach Python im Microsoft Store
   - Klicken Sie oben rechts auf das Suchsymbol
   - Geben Sie "Python" in die Suchleiste ein

3. Wählen Sie die Python-Version aus
   - Suchen Sie nach der neuesten Version von Python (zu Beginn des
     Schuljahres 24/25 ist das Python 3.12)
   - Klicken Sie auf den "Kostenlos"-Button neben der gewünschten Version

4. Installieren Sie Python
   - Warten Sie, bis der Download abgeschlossen ist
   - Klicken Sie den "Installieren"-Button
   - Während der Installation achten Sie darauf, dass die Option "Add
     Python to PATH" aktiviert ist. 
   - Der Download und die Installation können einige Minuten dauern,
     abhängig von Ihrer Internetverbindung 

5. Überprüfen Sie die Installation
   - Drücken Sie die Windows-Taste + R, um das "Ausführen"-Fenster zu öffnen
   - Geben Sie "cmd" ein und drücken Sie Enter, um die Eingabeaufforderung zu öffnen
   - Tippen Sie `python --version` und drücken Sie Enter
   - Wenn Python korrekt installiert wurde, sehen Sie die Versionsnummer

6. Testen Sie Python
   - Geben Sie in der Eingabeaufforderung "python" ein und drücken Sie Enter
   - Sie sollten nun die Python-Umgebung sehen
   - Tippen Sie "print('Hallo Welt!')" und drücken Sie Enter
   - Sie sollten "Hallo Welt!" als Ausgabe sehen
   - Um Python zu verlassen, tippen Sie "exit()" und drücken Sie Enter

Glückwunsch! Sie haben Python erfolgreich auf Ihrem Windows 11-Rechner
installiert und getestet.

## Installation zusätzlicher Werkzeuge

Für den Unterricht brauchen wir neben der Basisinstallation von Python
noch weitere Werkzeuge.

### "pip"

pip ist der Packet Installer für Python.  

Testen Sie die Installation von "pip":

- Öffnen Sie die Windows-Eingabeaufforderung (Terminal, cmd).
- Geben Sie im Terminal `pip --version` ein und drücken Sie Enter
- Wenn eine Versionsnummer angezeigt wird, ist "pip" erfolgreich
installiert 
- Falls nicht, geben Sie folgenden Befehl ein, um pip zu
installieren: 
`python -m ensurepip --upgrade`

### Jupyter Notebook

Jupyter Notebook ist eine Webanwendung, die Jupyter-Notebook-Dokumente
erstellen und bearbeiten kann. 

Ein Jupyter-Notebook-Dokument besteht aus einer Kombination von Text und
ausführbarem Programmcode. Jupyter Notebooks sind automatisch
versioniert. Die Dateinamen enden auf „.ipynb“. Ein Jupyter Notebook
kann in verschiedene Formate konvertiert und ausgegeben werden, z. B.
HTML, PDF, LaTeX und Folien für Präsentationen.

Für die Installation von Jupyter Notebooks
- Öffnen Sie die Windows-Eingabeaufforderung (cmd).
- Geben Sie folgenden Befehl ein, um Jupyter Notebooks zu installieren:
  `pip install notebook`
- Warten Sie, bis die Installation abgeschlossen ist.
- Jupyter Notebook aufrufbar machen (Jupyter Notebook zu PATH
  hinzufügen) 
- Installationspfad von Jupyter Notebook finden
  - Öffnen Sie Windows Explorer
  - Suchen Sie den Ordner mit Ihrer Python Installation (wahrscheinlich `C:\Users\<IhrBenutzername>\AppData\Local\Programs\Pyhton\Python312`)
  - Öffnen Sie mit Rechtsklick das Kontextmenü für den Ordner `Scripts`
    und wählen Sie "Als Pfad kopieren"
- Drücken Sie die **Windows-Taste** und geben Sie "Umgebungsvariablen
  für dieses Konto bearbeiten" in die Suchleiste ein 
- Im Fenster "Benutzervariablen für Benutzername" wählen Sie die
  Variabel "PATH" aus
- Klicken Sie auf "Bearbeiten"
- Klicken Sie im Fenster "Umgebungsvariablen bearbeiten" auf "Neu"
- Fügen Sie den zuvor kopierten Pfad ein (Ctrl V)
- Klicken Sie auf „OK“, um die Änderungen zu speichern
- Schließen Sie die Eingabeaufforderung und öffnen Sie sie erneut,
  damit die Änderungen wirksam werden 

- Überprüfung Sie die Änderungen
   - Geben Sie in der Eingabeaufforderung den folgenden Befehl ein, um zu überprüfen, ob Jupyter Notebook jetzt erkannt wird:
     ```
     jupyter notebook
     ```
   - Wenn alles korrekt eingerichtet ist, sollte sich Jupyter Notebook öffnen

- Um ein neues Notebook zu erstellen, klicken Sie auf "New" und wählen
  Sie "Python 3" 
- Sie können nun in den Zellen Python-Code eingeben und ausführen 
- Um Jupyter Notebooks zu beenden, schließen Sie das Browserfenster und
  drücken Sie in der Eingabeaufforderung Strg+C 

*Dieser Text wurde mit Hilfe von Perplexity.ai erstellt.*