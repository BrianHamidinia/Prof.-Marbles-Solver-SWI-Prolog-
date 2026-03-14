# Prof. Marbles – Prolog Solver (SWI-Prolog)

## Dateien

* Code/prof\_marbles\_solver.pl : Prolog-Solver (BFS, kürzeste Lösung)
* Code/tasks\_generated.pl     : Aufgaben (1..60), aus der TaskList generiert
* Code/export\_tasks\_to\_prolog.py : Generator, der die Aufgaben aus ProfMarblesTaskList.py nach Prolog exportiert

## Voraussetzungen

* SWI-Prolog (getestet mit SWI-Prolog 9.x)
* Optional: Python 3.x (nur zum erneuten Generieren der Aufgaben-Datei)

## Ausführen in SWI-Prolog

1. SWI-Prolog öffnen
2. In den Ordner "Code" wechseln (oder direkt per Pfad laden)
3. Dateien laden:

\['Code/prof\_marbles\_solver.pl'].

\['Code/tasks\_generated.pl'].

4. Beispiele:

   * solve\_task(1, Moves, N, Min).
   * run\_range(1,60).
   * run\_task\_verbose(40).

## Aufgaben generieren 

Im Ordner Code:
py export\_tasks\_to\_prolog.py > tasks\_generated.pl

