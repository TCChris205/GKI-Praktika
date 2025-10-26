# Prak 2

## 1

### Queens

#### Queens - Kodierung

Als Kodierung wird bei den Queens-Individuen eine zweidimensionale Liste verwendet, die alle Positionen der Königinnen als 1 einspeichert und alle leeren Felder mit einer 0 füllt. Dies ist sowohl eine sehr einfache und akkurate Darstellung des generierten Spielfelds, als auch eine gute Darstellung in Bit-Form, auf Basis welcher man die Fitness eines Individuums errechnen kann.

#### Queens - Selektion

Die Selektion findet über ein Turnier statt.

#### Queens - Crossover

Bei einem Crossover werden die 2D Listen der Individuen identisch an einer Stelle auf einer der Achsen geteilt und einer der beiden resultierenden Teile getauscht. Sollten dabei Königinnen verloren gehen oder dazukommen, werden zufällig Königinnen entfernt oder hinzugefügt, bis die Anzahl wiedeer stimmt.

#### Queens - Mutation

Bei der Mutation wird zu einer Chance von 10% die Position einer Dame zufällig neu gesetzt. Eine neu Platzierte Dame kann nicht auf dem selben Feld wie eine andere Dame landen.

#### Queens - Fitness

Die Fitness wird berechnet, indem für alle Damen alle von dieser betrachteten Felder, abgesehen von dem auf dem sie steht, in eine 2D Liste geschrieben werden. Am Ende hat man eine Liste mit allen betrachteten Feldern, anhand derer man schaut, wie viele Damen auf betrachteten Feldern stehen. Die Anzahl der "falsch" stehenden Damen wird vom Optimalwert der Fitness, 8, abgezogen.

### Countries

#### Countries - Kodierung

Als Kodierung wird bei den Countries primär ein Dictionary verwendet. Jedes Land kriegt einen Index zugeordnet und im Dictionary steht jedes Land mit seinen Nachbarländern. In einer seperaten Liste steht dann für jeden Landes-Index die dazugehörige Farbe, auch als Zahl kodiert. Die Anzahl der Farben ist begrenzt.
Das Dictionary ist vorher fest generiert in jedes Individuum integriert.
Das Dictionary wird benutzt, da es eine bereits implementierte Art und Weise bzw. Möglichkeit ist, die Länderverhältnisse Darzustellen, was die implementierung einer Eigenen Datenstruktur unnötig macht.

#### Countries - Selektion

Die Selektion findet über ein Turnier statt.

#### Countries - Crossover

Bei einem Crossover wird die Farbliste der Individuen identisch an einer Stelle geteilt und einer der beiden resultierenden Teile getauscht.

#### Countries - Mutation

Bei der Mutation wird zu einer Chance von 20% eine der Farben in der Farbliste durch eine andere zufällige ersetzt.

#### Countries - Fitness

Um die Fitness zu errechnen gibt es zwei Faktoren: Die Anzahl an angrenzenden Länder mit der selben Farbe und die Anzahl an verwendeten Farben. Hier wird für die Fitness ein Optimalwert von 7 angegeben und bei 10 gestartet, wobei für angrenzende Länder mit der selben Farbe 1 Punkte und pro Farbe 1 Punkt abgezogen werden. Indirekt wird für angrenzede Felder aber 2 abgezogen, da jedes Land individuell einen Punktabzug erzeugt: a->b und b->a ziehen jeweils einen Punkt ab. Als Optimalwert ist 7 angegeben, da von mindestens 3 verschiedenen Farben ausgegangen wird.

### Was würde man brauchen um das Problem mit Simulated Annealing zu lösen?

Eine Temperaturfunktion und eine spezifische Verschlechterungsakzeptanz.

## 2

### Auswertung Queens

- 1
  - Mutation Probability: 0.1
  - Crossover Probability: 0.6
  - Population: 100
  - TournamentSize: 10
  - Läufe: 100
  - MaxGenerationen: 100
  - Ergebnis:
    - 2 Treffer nach 3 und 7 Generationen, 7 nach 40+ Generationen. Rest Fehlschläge.
- 2
  - Mutation Probability: 0.1
  - Crossover Probability: 0.6
  - Population: 300
  - TournamentSize: 20
  - Läufe: 100
  - MaxGenerationen: 100
  - Ergebnis:
    - 25 Treffer, die meisten von ihnen im Bereich 30+ Generationen. Rest Fehlschläge.
- 1
  - Mutation Probability: 0.3
  - Crossover Probability: 0.6
  - Population: 100
  - TournamentSize: 10
  - Läufe: 100
  - MaxGenerationen: 100
  - Ergebnis:
    - 9 Treffer, einer Sofort. Keine Große Veränderung zum Fall 1, abgesehen von niedrigeren Durschnittsgenerationen.

#### Fazit Queens

Der Algorithmus läuft sehr langsam und findet meistens kein Ergebnis. Treffer sind entweder Zufällig recht Früh oder nach 50+ Generationen. Der Algorithmus hat wahrscheinlich zu viele Zufallsfaktoren, was ihn sehr verrauscht macht und die Idee von GA/EA nicht richtig ausnnutzt.

### Auswertung Countries

- 1
  - Mutation Probability: 0.1
  - Crossover Probability: 0.6
  - Population: 100
  - TournamentSize: 10
  - Läufe: 100
  - MaxGenerationen: 100
  - Ergebnis:
    - 94 Sofortige Treffer, 6 Mal nach einer Generation
- 2
  - Mutation Probability: 0.1
  - Crossover Probability: 0.6
  - Population: 10
  - TournamentSize: 3
  - Läufe: 100
  - MaxGenerationen: 100
  - Ergebnis:
    - 29 Sofortige Treffer, 6 Mal kein Treffer nach 100 Generationen, 23 Treffer unter 10, 42 über 10 Generationen
- 3
  - Mutation Probability: 0.3
  - Crossover Probability: 0.6
  - Population: 10
  - TournamentSize: 3
  - Läufe: 100
  - MaxGenerationen: 100
  - Ergebnis:
    - Mehr sofortige Treffer, deutlich niedrigerer Durchschnitt bei den benötigten Generationen, keine Fehlschläge, höchster Wert von 71

#### Fazit Countries

Der Algorithmus läuft recht schnell und auch ziemlich sicher. Bei kleinen Population kommt mehr Schwankung, die aber durch die wenigen tatsächlichen Variations-Möglichkeiten durch eine erhöhte Mutation wieder beseitigt werden können.

## 3

### 3.1

Die "Where's Waldo" Implementierung von EAs/GAs nimmt als Rechnungsgrundlage die Positionen aller Waldos innerhalb der ersten sieben "Where's Waldo"- Bücher. Ausgehend von diesen Punkten wird dann ein EA benutzt, um die Kostengünstigste Überprüfung der einzelnen Position, die Kosten gemessen an dem zurückgelegten Weg, zu finden. Gewissermaßen wurde das Problem also in ein Reisender-Händler-Problem umgewandelt. Die Implementierung bedient sich um die Fitness zu berechnen des gesamt zurückgelegten Weges und nutzt zur Mutation und Variation das vertauschen der Reihenfolgen der Besuchten Punkte und des austauschens ganzer Weges-Abschnitte.

### 3.2

Als Kodierung nutzt der Evolution Simulator eine gesamte generierte "Kreatur" aus Knoten und Muskeln, die durch gegebene Operatoren frei angepasst, verschoben, hinzugefügt und gelöscht werden können. Die Fitnessfunktion basiert auf der später simulierten Bewegung der Kreatur, wobei eine möglichst positive Distanz erreicht werden soll.

### 3.3

EAs/GAs werden im american fuzzy lop insoweit eingesetzt, das jedes Individuum probiert möglichst viele verschiedene und untypische Zustände in Code zu erzeugen. Durch die Generationen werden dann die Zustände des Codes immer Absurder gemacht, was zu einer sehr weitläufigen und tief-greifenden Testabdeckung weiterentwickelt wird.

### 3.4

Bei dem "Where's Waldo" Projekt ist die Fitness besser je kleiner sie ist und wurde implementiert, als das sie die Abstände aller Knoten addiert darstellt.

Bei dem Evolution Simulator wird die Fitness durch den Abstand der "Creature" vom Startpunkt angegeben. Je positiver der Abstand, desto besser. Bewegung in negative Richtung ist schlecht.

Bei dem American Fuzzy Lop hat sich die Fitnessfunktion nicht ganz herauskristallisiert und der Source Code wurde nicht betrachtet, da sofort eine Trojaner-Warnung aufgetaucht ist. Nach der Dokumentation scheint es aber so als würde die Fitnessfunktion bewerten, wie viele Crash-Möglichkeiten, spezielle Zustände oder Randzustände bei Variablen gefunden wurden. Jedes von denen erhöht die Fitness, gelistet in absteigender Reihenfolge. Je höher desto besser.

### 3.5

- Wirtschaft:
  - Verifikation von Prototypen
  - Entwurf von Netzwerken
  - Analyse von Aktienmärkten
- Forschung
  - Molekularbiologie
  - Künstliche Neuronale Netze
- Kunst und Musik
  - Generierung von speziellen, meist für Menschen möglichst angenehmen, Tonfolgen
