# Prof. Marbles Solver

Ein in **SWI-Prolog** entwickelter Solver für das Puzzle **Prof. Marbles**.  
Im Projekt habe ich das Spiel in Prolog modelliert, gültige Zugregeln umgesetzt und einen Solver mit **Breadth-First Search (BFS)** entwickelt, der **60 Puzzle-Instanzen automatisch** löst und **minimale Zugfolgen** berechnet.

## Projektinhalt
- Modellierung von Spielzuständen und Röhrenstrukturen in Prolog
- Implementierung der Zuglogik und Zustandsübergänge
- Entwicklung eines BFS-basierten Solvers zur Berechnung kürzester Lösungen
- Automatische Ausführung und Lösung von 60 Aufgaben
- Ausgabe von Zugfolge, Zuganzahl und Referenzwerten
- Unterstützung partieller Zielzustände
- Aufbereitung und Import der Aufgaben als Prolog-Fakten

## Start
In SWI-Prolog laden:

`['prof_marbles_solver.pl'].`  
`['tasks_generated.pl'].`

Beispiele:

`solve_task(1, Moves, N, MinExpected).`  
`run_range(1, 60).`  
`run_task_verbose(40).`

## Technologien
- SWI-Prolog
- Breadth-First Search (BFS)
- Python (optional zur Generierung der Task-Datei)

## Autor
Brayan Mohammad Hamidinia
