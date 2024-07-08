# Virtual Environments in Python

Python stellt sehr viele Pakete zu unterschiedlichen Problemstellungen
zur Verfügung. Um Installationen solcher Pakete gefahrlos ausprobieren
zu können, stellt Python virtuelle Arbeitsumgebungen zur Verfügung. 

Hier ist eine Schritt-für-Schritt-Anleitung zum Erstellen einer Python
Virtual Environment (venv) in einem vorgegebenen Ordner: 

1. Öffnen Sie die Eingabeaufforderung (cmd) oder PowerShell

2. Navigieren Sie zum gewünschten Ordner
   Verwenden Sie den Befehl:
   ```
   cd Pfad\zum\gewünschten\Ordner
   ```

   Alternativ kann die Eingabaufforderung (Terminal) auch geöffnet
   werden, indem im Windows Explorer mit
   Rechtsklick auf dem gewünschten Ordner im Kontextmenü "Öffnen im
   Terminal"  ausgewählt wird. Bei diesem Vorgehen öffnet das Terminal
   direkt im gewählten Ordner.

3. Erstellen Sie die Virtual Environment
   Geben Sie folgenden Befehl ein:
   ```
   python -m venv venv
   ```
   Dies erstellt einen Unterordner namens "venv" mit der Virtual Environment.

4. Aktivieren Sie die Virtual Environment
   Unter Windows:
   ```
   venv\Scripts\activate
   ```
   
5. Überprüfen Sie die Aktivierung
   Sie sollten nun (venv) am Anfang der Eingabeaufforderung sehen.

6. Installieren Sie benötigte Pakete
   Verwenden Sie pip, um Pakete zu installieren, z.B.:
   ```
   pip install paketname
   ```

7. Deaktivieren der Virtual Environment
   Wenn Sie fertig sind, geben Sie ein:
   ```
   deactivate
   ```


*Dieser Text wurde mit Hilfe von Perplexity.ai erstellt.*