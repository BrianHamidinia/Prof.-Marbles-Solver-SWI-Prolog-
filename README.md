# Prof. Marbles Solver

Ein in **SWI-Prolog** entwickelter Solver für das Puzzle **Prof. Marbles**.
Das Projekt löst **60 Aufgaben automatisch** und verwendet **Breadth-First Search (BFS)**, um **minimale Zugfolgen** zu berechnen.

## Funktionen
- Automatische Lösung von Task 1 bis 60
- Berechnung kürzester Zugfolgen mit BFS
- Ausgabe von Zugfolge und Zuganzahl
- Unterstützung partieller Zielzustände

## Start
In SWI-Prolog laden:

['prof_marbles_solver.pl'].
['tasks_generated.pl'].

Beispiele:

solve_task(1, Moves, N, MinExpected).
run_range(1, 60).
run_task_verbose(40).

## Technologien
- SWI-Prolog
- Python (optional zur Generierung der Task-Datei)

## Autor
Mohammad (Brayen) Hamidinia
