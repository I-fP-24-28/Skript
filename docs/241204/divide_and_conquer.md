# Rekursion

Bevor ein etwas effizienterer Sortieralgorithmus als selection sort besprochen
werden kann, muss ein weiteres Programmierverfahren eingeführt werden: Die
Rekursion. Man spricht in diesem Zusammenhang gelegentlich auch von *divide and
conquer* (teile und herrsche).

Die Möglichkeiten und Grenzen der Rekursion soll mit Hilfe dreier Beispiele

* der Berechnung der Summe einer Sequenz aufsteigender Zahlen,
* der Berechnung des Produkts einer Sequenz aufsteigender Zahlen ($n!$) sowie
* der Fibonacci Zahlenfolge

aufgezeigt werden.

Wie Rekursion im Allgemeinen funktioniert, kann mit der folgenden
Kindergeschichte aufgezeigt werden:

>Es isch e mal en Maa gsi, de hät en hole Zah gha. I dem Zah häts es
>Truckli gha und i däm Truckli häts es Briefli gha. I dem Briefli isch
>gstande, es isch e mal en Maa gsi, de hät en hole Zah gha. I dem Zah
>häts es Truckli gha und id däm Truckli häts es Briefli gha...

Rekursive Funktionen sind entsprechend Funktionen, die sich selber
aufrufen. 

Hier geht es zu einem 
[Arbeitsblatt zu den rekursiven Funktionen](anwendungsuebung_rekursion.ipynb).  
Die Musterlösung des Arbeitsblattes ist hier <a
hrfef="https://colab.research.google.com/github/I-fP-24-28/Skript/blob/main/docs/241204/musterloesung_anwendungsuebung_rekursion.ipynb"
target="_blank">verlinkt</a>.