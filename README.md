# Prof. Marbles Solver

Ein in **SWI-Prolog** entwickelter Solver für das Puzzle **Prof. Marbles**.  
Das Projekt löst **60 Puzzle-Instanzen automatisch** und berechnet mit **Breadth-First Search (BFS)** **minimale Zugfolgen**.

## Projektinhalt
- Modellierung des Spiels und der Zustände in Prolog
- Implementierung gültiger Zugregeln
- Automatische Lösung von 60 Aufgaben
- Berechnung kürzester Lösungen mit BFS
- Ausgabe von Zugfolge und Zuganzahl
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
Mohammad (Brayen) Hamidinia
