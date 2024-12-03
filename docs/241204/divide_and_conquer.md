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

Bevor der Algorithmus von Merge Sort besprochen wird, soll an ein paar 
[Beispielen](https://colab.research.google.com/github/I-gW-23-27/Skript/blob/main/docs/240312/src/rekursion.ipynb) 
gezeigt werden, wie rekursiv implementierte Problemlösungen
funktionieren. Hier finden Sie die illustrierte
[Musterlösung](https://colab.research.google.com/github/I-gW-23-27/Skript/blob/main/docs/240312/src/rekursion_muloe.ipynb)
(stand 24. März 24).
