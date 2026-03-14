% ============================================
% Prof. Marbles Solver (SWI-Prolog)
% Move = "stuelpen" (flip one tube onto another)
% -> balls transfer into destination in REVERSED order
% -> destination fills empty places; remaining balls stay in source
%
% Tube representation:
%   tube(Capacity, BallsBottomToTop)
%   (empty slots are implicit; no 'e' stored in state)
%
% Task representation:
%   task(TaskNo, MinExpected, StartTubes, GoalTubes).
%   GoalTubes can be partial (only listed tubes must match).
%
% Main predicates:
%   solve_task(TaskNo, Moves, N).
%   solve_task(TaskNo, Moves, N, MinExpected).
%   run_range(From, To).
% ============================================

:- use_module(library(lists)).
:- use_module(library(assoc)).

% ----------- Public API -----------
solve_task(TaskNo, Moves, N) :-
    task(TaskNo, _MinExpected, Start0, Goal0),
    sort_tubes(Start0, Start),
    sort_tubes(Goal0, Goal),
    bfs(Start, Goal, Moves),
    length(Moves, N).

solve_task(TaskNo, Moves, N, MinExpected) :-
    task(TaskNo, MinExpected, Start0, Goal0),
    sort_tubes(Start0, Start),
    sort_tubes(Goal0, Goal),
    bfs(Start, Goal, Moves),
    length(Moves, N).

print_moves([]).
print_moves([move(F,T)|Ms]) :-
    format("stuelpen: tube ~w -> tube ~w~n", [F,T]),
    print_moves(Ms).

% ----------- Goal check (tube constraints from Goal must match) -----------
% Goal tubes are constraints: only those tubes listed in Goal must match.
% We compare the FULL tube content bottom->top including empty slots.
goal_reached(State, Goal) :-
    forall(member(tube(CapG, GoalBalls), Goal),
           tube_matches(State, CapG, GoalBalls)).

tube_matches(State, Cap, GoalBalls) :-
    member(tube(Cap, StateBalls), State),
    pad_to_capacity(Cap, StateBalls, StateFull),
    pad_to_capacity(Cap, GoalBalls, GoalFull),
    StateFull = GoalFull.

pad_to_capacity(Cap, Balls, Full) :-
    length(Balls, L),
    Missing is Cap - L,
    Missing >= 0,
    make_n(Missing, e, Es),
    append(Balls, Es, Full).

make_n(0, _, []) :- !.
make_n(N, X, [X|Xs]) :-
    N > 0,
    N1 is N - 1,
    make_n(N1, X, Xs).


% counts(Tubes, R, Y, G, E)
% Here we count r/y/g from Balls, and compute E using tube capacities.
counts(Tubes, R, Y, G, E) :-
    findall(B, (member(tube(_Cap, Balls), Tubes), member(B, Balls)), All),
    count_color(r, All, R),
    count_color(y, All, Y),
    count_color(g, All, G),
    total_capacity(Tubes, CapSum),
    length(All, Filled),
    E is CapSum - Filled.

total_capacity([], 0).
total_capacity([tube(Cap, _)|Ts], Sum) :-
    total_capacity(Ts, S1),
    Sum is S1 + Cap.

count_color(C, List, N) :-
    include(==(C), List, Filtered),
    length(Filtered, N).


% ----------- Canonical ordering -----------
sort_tubes(Tubes, Sorted) :-
    predsort(compare_tube_cap, Tubes, Sorted).

compare_tube_cap(Order, tube(C1,_), tube(C2,_)) :-
    compare(Order, C1, C2).

% ----------- Move (stuelpen) -----------
% move(State, NextState, move(FromCap, ToCap))
move(State, NextState, move(FromCap, ToCap)) :-
    select(tube(FromCap, SrcBalls), State, Rest1),
    select(tube(ToCap, DstBalls), Rest1, Rest2),
    stuelpen_transfer(ToCap, SrcBalls, DstBalls, NewSrc, NewDst),
    sort_tubes([tube(FromCap, NewSrc), tube(ToCap, NewDst) | Rest2], NextState).

% stuelpen_transfer(DstCap, SrcBalls, DstBalls, NewSrcBalls, NewDstBalls)
% Transfers as many balls as fit into destination.
% Transfer order is reverse(SrcBalls).
stuelpen_transfer(DstCap, SrcBalls, DstBalls, NewSrc, NewDst) :-
    SrcBalls \= [],
    length(DstBalls, LD),
    Space is DstCap - LD,
    Space > 0,
    reverse(SrcBalls, RevSrc),
    take_drop(Space, RevSrc, Taken, RemRev),
    Taken \= [],                 % ensure it changes state (no-op not allowed)
    append(DstBalls, Taken, NewDst),
    reverse(RemRev, NewSrc).

% take_drop(N, List, Taken, Rest)
take_drop(N, List, Taken, Rest) :-
    (   N =< 0
    ->  Taken = [], Rest = List
    ;   take_drop_(N, List, Taken, Rest)
    ).

take_drop_(_N, [], [], []).
take_drop_(N, [X|Xs], [X|Ts], Rest) :-
    N > 0,
    N1 is N - 1,
    take_drop_(N1, Xs, Ts, Rest).
take_drop_(0, Rest, [], Rest).

% ----------- BFS (shortest path) -----------
bfs(Start, Goal, Moves) :-
    empty_assoc(V0),
    put_assoc(Start, V0, true, Visited),
    bfs_loop([node(Start, [])], Visited, Goal, MovesRev),
    reverse(MovesRev, Moves).

bfs_loop([node(State, PathRev)|_], _Visited, Goal, PathRev) :-
    goal_reached(State, Goal),
    !.

bfs_loop([node(State, PathRev)|Queue], Visited0, Goal, MovesRev) :-
    findall(node(Next, [M|PathRev]),
            ( move(State, Next, M),
              \+ get_assoc(Next, Visited0, _)
            ),
            NewNodes),
    mark_visited(NewNodes, Visited0, Visited1),
    append(Queue, NewNodes, Queue2),
    bfs_loop(Queue2, Visited1, Goal, MovesRev).

mark_visited([], Visited, Visited).
mark_visited([node(S,_)|Ns], Visited0, Visited2) :-
    put_assoc(S, Visited0, true, Visited1),
    mark_visited(Ns, Visited1, Visited2).

% ----------- Batch run helpers -----------
run_tasks([]).
run_tasks([T|Ts]) :-
    (   task(T, _, _, _)
    ->  (   solve_task(T, _Moves, N, Min)
        ->  format("Task ~w: solved in ~w moves (min: ~w)~n", [T, N, Min])
        ;   format("Task ~w: defined but NOT solvable with current solver/rules.~n", [T])
        )
    ;   format("Task ~w: NOT DEFINED (missing task(~w,...)).~n", [T, T])
    ),
    run_tasks(Ts).


run_range(From, To) :-
    findall(T, between(From, To, T), Ts),
    run_tasks(Ts).

run_task_verbose(T) :-
    solve_task(T, Moves, N, Min),
    format("Task ~w: solved in ~w moves (min: ~w)~n", [T, N, Min]),
    print_moves(Moves).

% --- Check existence of a solution with EXACTLY K moves (no BFS) ---
exists_solution_in_k_moves(TaskNo, K, Moves) :-
    task(TaskNo, _Min, Start0, Goal0),
    sort_tubes(Start0, Start),
    sort_tubes(Goal0, Goal),
    path_k(Start, Goal, K, [], MovesRev),
    reverse(MovesRev, Moves).

path_k(State, Goal, 0, Moves, Moves) :-
    goal_reached(State, Goal), !.
path_k(State, Goal, K, Acc, Moves) :-
    K > 0,
    move(State, Next, M),
    K1 is K - 1,
    path_k(Next, Goal, K1, [M|Acc], Moves).

% ----------- Tasks (generated from ProfMarblesTaskList.py) -----------

task(1, 2,
     [tube(4,[r,r,r,y]), tube(3,[]), tube(2,[])],
     [tube(3,[y])]).

task(2, 2,
     [tube(5,[r,y,r,y,r]), tube(4,[]), tube(2,[])],
     [tube(2,[y,r])]).

task(3, 2,
     [tube(4,[y,r]), tube(3,[r,r]), tube(2,[])],
     [tube(2,[y])]).

task(4, 2,
     [tube(4,[]), tube(3,[r,r,y]), tube(2,[])],
     [tube(2,[r,r])]).

task(5, 3,
     [tube(4,[r,r,r,y]), tube(3,[]), tube(2,[])],
     [tube(2,[y])]).

task(6, 3,
     [tube(7,[r,y,y,r,r,y]), tube(4,[]), tube(2,[])],
     [tube(7,[r,y]), tube(4,[r,y]), tube(2,[r,y])]).

task(7, 3,
     [tube(5,[r,y,r,y,r]), tube(4,[]), tube(3,[])],
     [tube(5,[r,r])]).

task(8, 3,
     [tube(4,[r]), tube(3,[r]), tube(2,[y,r])],
     [tube(4,[r]), tube(3,[r]), tube(2,[r,y])]).

task(9, 3,
     [tube(4,[g]), tube(3,[y]), tube(2,[r])],
     [tube(3,[g,y,r])]).

task(10, 3,
     [tube(5,[r,y]), tube(4,[r,r]), tube(2,[r,r])],
     [tube(5,[r,r]), tube(4,[r,r]), tube(2,[r,y])]).

task(11, 4,
     [tube(4,[r,y,y]), tube(3,[g,g,r]), tube(2,[])],
     [tube(4,[r,r]), tube(3,[y,y]), tube(2,[g,g])]).

task(12, 4,
     [tube(5,[r,r,r,y,y]), tube(3,[]), tube(2,[])],
     [tube(3,[y,r,y])]).

task(13, 4,
     [tube(5,[r,y,r,y,r]), tube(4,[]), tube(2,[])],
     [tube(2,[r,r])]).

task(14, 4,
     [tube(5,[r,r,r]), tube(3,[y,r,r]), tube(2,[])],
     [tube(5,[r,r,y]), tube(3,[r,r,r])]).

task(15, 4,
     [tube(4,[]), tube(3,[r,r]), tube(2,[r,y])],
     [tube(4,[r]), tube(3,[r]), tube(2,[r,y])]).

task(16, 5,
     [tube(7,[r,y,y,r,r,y]), tube(5,[]), tube(2,[])],
     [tube(7,[y,r]), tube(5,[y,r]), tube(2,[y,r])]).

task(17, 5,
     [tube(5,[r]), tube(3,[r,y,r]), tube(2,[r])],
     [tube(5,[r]), tube(3,[r,r,y]), tube(2,[r])]).

task(18, 5,
     [tube(4,[r]), tube(3,[y]), tube(2,[g,g])],
     [tube(4,[g]), tube(3,[g]), tube(2,[y,r])]).

task(19, 5,
     [tube(7,[y,r,g]), tube(5,[y,r]), tube(2,[y,r])],
     [tube(7,[y,r]), tube(5,[y,r,g]), tube(2,[y,r])]).

task(20, 5,
     [tube(4,[r,y,r,r]), tube(3,[]), tube(2,[])],
     [tube(4,[y])]).

task(21, 5,
     [tube(6,[y,r,r,r,r,g]), tube(3,[]), tube(4,[])],
     [tube(6,[y]), tube(4,[r,r,r,r]), tube(3,[g])]).

task(22, 6,
     [tube(4,[r,g,y,r]), tube(3,[]), tube(2,[])],
     [tube(4,[g]), tube(3,[y]), tube(2,[r,r])]).

task(23, 6,
     [tube(6,[r,r,y,r,r,r]), tube(3,[]), tube(2,[])],
     [tube(3,[y])]).

task(24, 6,
     [tube(6,[y,r,r,r,y,y]), tube(4,[]), tube(3,[])],
     [tube(3,[r,r,r])]).

task(25, 6,
     [tube(5,[y,r]), tube(3,[r,r,r]), tube(2,[])],
     [tube(5,[r,r,r,r])]).

task(26, 6,
     [tube(5,[]), tube(3,[r,y,r]), tube(2,[])],
     [tube(2,[y])]).

task(27, 6,
     [tube(4,[g]), tube(3,[y,y,y]), tube(2,[r])],
     [tube(3,[g,y,r])]).

task(28, 7,
     [tube(7,[r,r,r,r,r,r,y]), tube(4,[]), tube(3,[])],
     [tube(7,[y,r,r,r,r,r,r])]).

task(29, 7,
     [tube(7,[r,r,r,r,r]), tube(5,[]), tube(3,[y,r])],
     [tube(3,[y])]).

task(30, 7,
     [tube(4,[]), tube(3,[g,r,y]), tube(2,[g,r])],
     [tube(4,[y]), tube(3,[g,r]), tube(2,[g,r])]).

task(31, 7,
     [tube(4,[r]), tube(3,[r,y,y]), tube(2,[r])],
     [tube(4,[y]), tube(3,[r,r,r]), tube(2,[y])]).

task(32, 7,
     [tube(4,[r,y]), tube(3,[r]), tube(2,[r,r])],
     [tube(4,[y])]).

task(33, 7,
     [tube(5,[y,r]), tube(3,[r,r,r]), tube(2,[])],
     [tube(2,[y])]).

task(34, 8,
     [tube(8,[r,y,r,r,r,r,r,r]), tube(5,[]), tube(4,[])],
     [tube(5,[y])]).

task(35, 8,
     [tube(8,[r,r,r,r,y,y,y,y]), tube(6,[]), tube(3,[])],
     [tube(6,[r,r,y,y,r,r])]).

task(36, 8,
     [tube(6,[y,y]), tube(4,[g,g]), tube(3,[r,r,r])],
     [tube(6,[g,g]), tube(4,[y,y]), tube(3,[r,r,r])]).

task(37, 8,
     [tube(6,[r,r,r,y,y,g]), tube(4,[]), tube(3,[])],
     [tube(6,[g]), tube(4,[y,y]), tube(3,[r,r,r])]).

task(38, 9,
     [tube(5,[y,y,r,r,r]), tube(3,[]), tube(2,[])],
     [tube(5,[r,y,r,y,r])]).

task(39, 9,
     [tube(7,[g,r,r,r,r,r,y]), tube(4,[]), tube(3,[])],
     [tube(7,[y,r,r,r,r,r,g])]).

task(40, 2,
     [tube(7,[r,y,r,g,y,r,y]), tube(5,[]), tube(2,[])],
     [tube(7,[r,y,g]), tube(5,[r,y]), tube(2,[r,y])]).

task(41, 9,
     [tube(5,[g,r]), tube(3,[g,r,y]), tube(2,[])],
     [tube(5,[r,r]), tube(3,[y]), tube(2,[g,g])]).

task(42, 9,
     [tube(4,[g]), tube(3,[y,y,y]), tube(2,[r])],
     [tube(4,[r]), tube(3,[y,y,y]), tube(2,[g])]).

task(43, 10,
     [tube(8,[r,r,r,r,y,y,y,y]), tube(5,[]), tube(3,[])],
     [tube(8,[y,y,r,r,y,y,r,r])]).

task(44, 10,
     [tube(7,[r,y,g,r,y,g,r]), tube(5,[]), tube(3,[])],
     [tube(5,[r,r,r,y,y])]).

task(45, 10,
     [tube(6,[g,r,r,r,r,y]), tube(4,[]), tube(3,[])],
     [tube(6,[y]), tube(4,[r,r,r,r]), tube(3,[g])]).

task(46, 11,
     [tube(6,[r]), tube(4,[y,y,y,y]), tube(3,[g])],
     [tube(6,[g]), tube(4,[y,y,y,y]), tube(3,[r])]).

task(47, 11,
     [tube(8,[r,r,r,r,r,g]), tube(7,[y,y]), tube(3,[])],
     [tube(8,[r,r,r,r,g,r]), tube(7,[y,y])]).

task(48, 11,
     [tube(8,[r,g,r,y,r,g,r,y]), tube(6,[]), tube(3,[])],
     [tube(6,[y,r,r,r,r,y])]).

task(49, 11,
     [tube(6,[r,y,r,r,g,r]), tube(4,[]), tube(3,[])],
     [tube(6,[y]), tube(4,[r,r,r,r]), tube(3,[g])]).

task(50, 11,
     [tube(7,[y,r,r]), tube(6,[r,g,r]), tube(3,[r,r,y])],
     [tube(7,[g]), tube(6,[y,r,r,r,r,r]), tube(3,[y,r])]).

task(51, 12,
     [tube(8,[r,r,y,y]), tube(6,[y,r,y,r]), tube(3,[])],
     [tube(8,[r,r,y,y]), tube(6,[r,r,y,y])]).

task(52, 12,
     [tube(8,[y,y,r,r,g,g,g,g]), tube(5,[]), tube(3,[])],
     [tube(3,[g,y,r])]).

task(53, 13,
     [tube(8,[r,y,g]), tube(7,[r,y,g]), tube(3,[r,y,g])],
     [tube(8,[g,g,g]), tube(7,[y,y,y]), tube(3,[r,r,r])]).

task(54, 13,
     [tube(8,[r,r,r,r,r]), tube(7,[g,y,y]), tube(3,[])],
     [tube(8,[r,g,r,r,r,r]), tube(7,[y,y])]).

task(55, 14,
     [tube(8,[r,r,r,r,y,y,y,y]), tube(5,[]), tube(4,[])],
     [tube(8,[r,y,r,y,r,y,r,y])]).

task(56, 14,
     [tube(7,[g]), tube(5,[r,y,r,y,r]), tube(3,[g,y,g])],
     [tube(7,[g,g,g]), tube(5,[y,y,y]), tube(3,[r,r,r])]).

task(57, 16,
     [tube(8,[g,g,g]), tube(7,[y,y,y]), tube(3,[r,r,r])],
     [tube(8,[g,y,r]), tube(7,[g,y,r]), tube(3,[g,y,r])]).

task(58, 16,
     [tube(8,[r,y,r,r,r,r,y,g]), tube(5,[]), tube(4,[])],
     [tube(8,[g]), tube(5,[r,r,r,r,r]), tube(4,[y,y])]).

task(59, 17,
     [tube(7,[r,r,g,g,y,r,y]), tube(4,[]), tube(3,[])],
     [tube(7,[g,g]), tube(4,[y,y]), tube(3,[r,r,r])]).

task(60, 18,
     [tube(8,[g,y,g,y]), tube(6,[r,r,r,r]), tube(3,[])],
     [tube(8,[g,g,y,y]), tube(6,[r,r,r,r])]).

% total: 60 tasks

