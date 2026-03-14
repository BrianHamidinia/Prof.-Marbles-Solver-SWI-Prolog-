using System;
using System.Collections.Generic;
using System.Linq;
using m = ProfMarblesTasks.MarblePosition;

namespace ProfMarblesTasks
{
    public class ProfMarblesTaskList
    {
        public List<MarbleTask> GameTasks { get; set; }

        public ProfMarblesTaskList()
        {
            m r = m.red;
            m y = m.yellow;
            m g = m.green;
            m e = m.empty;

            GameTasks = new List<MarbleTask>();

            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, y), Tube(3), Tube(2)),
                Tubes(Tube(y, e, e)),
                2, 1));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, y, r), Tube(e, e, e, e), Tube(e, e)),
                Tubes(Tube(y, r)),
                2, 2));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(y, r, e, e), Tube(r, r, e), Tube(2)),
                Tubes(Tube(y, e)),
                2, 3));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(e, e, e, e), Tube(r, r, y), Tube(2)),
                Tubes(Tube(r, r)),
                2, 4));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, y), Tube(3), Tube(2)),
                Tubes(Tube(y, e)),
                3, 5));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, y, r, r, y, e), Tube(4), Tube(2)),
                Tubes(Tube(r, y, e, e, e, e, e), Tube(r, y, e, e), Tube(r, y)),
                3, 6));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, y, r), Tube(4), Tube(3)),
                Tubes(Tube(r, r, e, e, e)),
                3, 7));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4, r), Tube(3, r), Tube(y, r)),
                Tubes(Tube(4, r), Tube(3, r), Tube(r, y)),
                3, 8));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4, g), Tube(3, y), Tube(2, r)),
                Tubes(Tube(g, y, r)), // Laut Abbildung aber im 4er Glas
                3, 9));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(5, r, y), Tube(4, r, r), Tube(r, r)),
                Tubes(Tube(5, r, r), Tube(4, r, r), Tube(r, y)),
                3, 10));

            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, y, e), Tube(g, g, r), Tube(2)),
                Tubes(Tube(4, r, r), Tube(3, y, y), Tube(g, g)),
                4, 11));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, y, y), Tube(3), Tube(2)),
                Tubes(Tube(y, r, y)),
                4, 12));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, y, r), Tube(4), Tube(2)),
                Tubes(Tube(r, r)),
                4, 13));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(5, r, r, r), Tube(y, r, r), Tube(2)),
                Tubes(Tube(5, r, r, y), Tube(r, r,r )),
                4, 14));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4), Tube(r, r, e), Tube(r, y)),
                Tubes(Tube(4, r), Tube(3, r), Tube(r, y)),
                4, 15));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, y, r, r, y, e), Tube(5), Tube(2)),
                Tubes(Tube(7, y, r), Tube(5, y, r), Tube(y, r)),
                5, 16));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(5, r), Tube(r, y, r), Tube(r, e)),
                Tubes(Tube(5, r), Tube(r, r, y), Tube(r, e)),
                5, 17));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4, r), Tube(3, y), Tube(g, g)),
                Tubes(Tube(4, g), Tube(3, g), Tube(y, r)),
                5, 18));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(7, y, r, g), Tube(5, y, r), Tube(y, r)),
                Tubes(Tube(7, y, r), Tube(5, y, r, g), Tube(y, r)),
                5, 19));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, r), Tube(3), Tube(2)),
                Tubes(Tube(4, y)),
                5, 20));


            GameTasks.Add(new MarbleTask(
                Tubes(Tube(y, r, r, r, r, g), Tube(3), Tube(4)),
                Tubes(Tube(6, y), Tube(r, r, r, r), Tube(3, g)),
                5, 21));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, g, y, r), Tube(3), Tube(2)),
                Tubes(Tube(4, g), Tube(3, y), Tube(r, r)),
                6, 22));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, y, r, r, r), Tube(3), Tube(2)),
                Tubes(Tube(3, y)),
                6, 23));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(y, r, r, r, y, y), Tube(4), Tube(3)),
                Tubes(Tube(r, r, r)),
                6, 24));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(5, y, r), Tube(r, r, r), Tube(2)),
                Tubes(Tube(r, r, r, r, e)),
                6, 25));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(5), Tube(r, y, r), Tube(2)),
                Tubes(Tube(y, e)),
                6, 26));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4, g), Tube(y, y, y), Tube(r, e)),
                Tubes(Tube(g, y, r)),
                6, 27));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, r, r, r, y), Tube(4), Tube(3)),
                Tubes(Tube(y, r, r, r, r, r, r)),
                7, 28));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(7, r, r, r, r, r), Tube(5), Tube(y, r, e)),
                Tubes(Tube(3, y)),
                7, 29));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4), Tube(g, r, y), Tube(g, r)),
                Tubes(Tube(4, y), Tube(g, r, e), Tube(g, r)),
                7, 30));


            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4, r), Tube(r, y, y), Tube(r, e)),
                Tubes(Tube(4, y), Tube(r, r, r), Tube(y, e)),
                7, 31));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4, r, y), Tube(3, r), Tube(r, r)),
                Tubes(Tube(4, y)),
                7, 32));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(5, y, r), Tube(r, r, r), Tube(2)),
                Tubes(Tube(y, e)),
                7, 33));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, r, r, r, r, r), Tube(5), Tube(4)),
                Tubes(Tube(5, y)),
                8, 34));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, r, y, y, y, y), Tube(6), Tube(3)),
                Tubes(Tube(r, r, y, y, r, r)),
                8, 35));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(6, y, y), Tube(4, g, g), Tube(r, r, r)),
                Tubes(Tube(6, g, g), Tube(4, y, y), Tube(r, r, r)),
                8, 36));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, y, y, g), Tube(4), Tube(3)),
                Tubes(Tube(6, g), Tube(4, y, y), Tube(r, r, r)),
                8, 37));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(y, y, r, r, r), Tube(3), Tube(2)),
                Tubes(Tube(r, y, r, y, r)),
                9, 38));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(g, r, r, r, r, r, y), Tube(4), Tube(3)),
                Tubes(Tube(y, r, r, r, r, r, g)),
                9, 39));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, g, y, r, y), Tube(5), Tube(2)),
                Tubes(Tube(7, r, y, g), Tube(5, r, y), Tube(r, y)),
                2, 40));


            GameTasks.Add(new MarbleTask(
                Tubes(Tube(5, g, r), Tube(g, r, y), Tube(2)),
                Tubes(Tube(5, r, r), Tube(3, y), Tube(g, g)),
                9, 41));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(4, g), Tube(y, y, y), Tube(r, e)),
                Tubes(Tube(4, r), Tube(y, y, y), Tube(g, e)),
                9, 42));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, r, y, y, y, y), Tube(5), Tube(3)),
                Tubes(Tube(y, y, r, r, y, y, r, r)),
                10, 43));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, g, r, y, g, r), Tube(5), Tube(3)),
                Tubes(Tube(r, r, r, y, y)),
                10, 44));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(g, r, r, r, r, y), Tube(4), Tube(3)),
                Tubes(Tube(6, y), Tube(r, r, r, r), Tube(3, g)),
                10, 45));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(6, r), Tube(y, y, y, y), Tube(3, g)),
                Tubes(Tube(6, g), Tube(y, y, y, y), Tube(3, r)),
                11, 46));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(8, r, r, r, r, r, g), Tube(7, y, y), Tube(3)),
                Tubes(Tube(8, r, r, r, r, g, r), Tube(7, y, y)),
                11, 47));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, g, r, y, r, g, r, y), Tube(6), Tube(3)),
                Tubes(Tube(y, r, r, r, r, y)),
                11, 48));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, r, g, r), Tube(4), Tube(3)),
                Tubes(Tube(6, y), Tube(r, r, r, r), Tube(3, g)),
                11, 49));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(7, y, r, r), Tube(6, r, g, r), Tube(r, r, y)),
                Tubes(Tube(7, g), Tube(y, r, r, r, r, r), Tube(y, r, e)),
                11, 50));


            GameTasks.Add(new MarbleTask(
                Tubes(Tube(8, r, r, y, y), Tube(6, y, r, y, r), Tube(3)),
                Tubes(Tube(8, r, r, y, y), Tube(6, r, r, y, y)),
                12, 51));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(y, y, r, r, g, g, g, g), Tube(5), Tube(3)),
                Tubes(Tube(g, y, r)),
                12, 52));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(8, r, y, g), Tube(7, r, y, g), Tube(r, y, g)),
                Tubes(Tube(8, g, g, g), Tube(7, y, y, y), Tube(r, r, r)),
                13, 53));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(8, r, r, r, r, r), Tube(7, g, y, y), Tube(3)),
                Tubes(Tube(8, r, g, r, r, r, r), Tube(7, y, y)),
                13, 54));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, r, r, y, y, y, y), Tube(5), Tube(4)),
                Tubes(Tube(r, y, r, y, r, y, r, y)),
                14, 55));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(7, g), Tube(r, y, r, y, r), Tube(g, y, g)),
                Tubes(Tube(7, g, g, g), Tube(5, y, y, y), Tube(r, r, r)),
                14, 56));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(8, g, g, g), Tube(7, y, y, y), Tube(r, r, r)),
                Tubes(Tube(8, g, y, r), Tube(7, g, y, r), Tube(g, y, r)),
                16, 57));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, y, r, r, r, r, y, g), Tube(5), Tube(4)),
                Tubes(Tube(8, g), Tube(r, r, r, r, r), Tube(4, y, y)),
                16, 58));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(r, r, g, g, y, r, y), Tube(4), Tube(3)),
                Tubes(Tube(7, g, g), Tube(4, y, y), Tube(r, r, r)),
                17, 59));
            GameTasks.Add(new MarbleTask(
                Tubes(Tube(8, g, y, g, y), Tube(6, r, r, r, r), Tube(3)),
                Tubes(Tube(8, g, g, y, y), Tube(6, r, r, r, r)),
                18, 60));

            List<int> fails = new List<int>();
            if(!ValidateTasks(fails))
            {
                string failList = string.Join(", ", fails.Select(i => i.ToString())).TrimEnd(", ".ToCharArray());
                throw new Exception($"Some of the tasks are configured faulty: {failList}");
            }
        }

        private bool ValidateTasks(List<int> fails)
        {
            fails.Clear();

            foreach (MarbleTask task in GameTasks)
            {
                if (!Validate(task.StartConditions, task.Goal))
                {
                    fails.Add(task.Name);
                }
            }
            return fails.Count == 0;
        }

        private bool Validate(List<TestTube> start, List<TestTube> goal)
        {
            GetCount(start, out int rS, out int yS, out int gS, out int eS);
            GetCount(goal, out int rG, out int yG, out int gG, out int eG);
            int startSum = rS + yS + gS + eS;
            int goalSum = rG + yG + gG + eG;

            if(startSum == goalSum)
            {
                return rS == rG && yS == yG && gS == gG && eS == eG;
            }
            else
            {
                return rS >= rG && yS >= yG && gS >= gG && eS >= eG;
            }
        }

        private void GetCount(List<TestTube> tubes, out int r, out int y, out int g, out int e)
        {
            r = 0;
            y = 0;
            g = 0;
            e = 0;

            foreach (TestTube tube in tubes)
            {
                foreach (m marble in tube)
                {
                    switch (marble)
                    {
                        case m.red:
                            r++;
                            break;
                        case m.green:
                            g++;
                            break;
                        case m.yellow:
                            y++;
                            break;
                        case m.empty:
                            e++;
                            break;
                        default:
                            throw new Exception($"Unexpected marble: {marble}");
                    }
                }
            }
        }

        public static List<TestTube> Tubes(params TestTube[] tubes)
        {
            return tubes.ToList();
        }

        public static TestTube Tube(params m[] positions)
        {
            return new TestTube(positions);
        }

        public static TestTube Tube(int size, params m[] positions)
        {
            var positionList = positions.ToList();
            for (int i = 0; i < size - positions.Length; i++)
            {
                positionList.Add(m.empty);
            }
            return Tube(positionList.ToArray());
        }

        public static TestTube Tube(int size)
        {
            List<m> marblePositions = new List<m>();
            for (int i = 0; i < size; i++)
            {
                marblePositions.Add(m.empty);
            }
            return Tube(marblePositions.ToArray());
        }
    }
}
