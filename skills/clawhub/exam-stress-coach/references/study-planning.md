# Evidence-Based Study Planning

This document explains the cognitive science behind the Exam Stress Coach study planner and how it translates principles into a concrete schedule.

## Core Principles

### 1. Distributed Practice (Spaced Repetition)

**Principle:** Spreading study sessions across multiple days produces dramatically better retention than cramming the same total time into one session.

**Key finding:** Cepeda et al. (2008) meta-analyzed 254 studies and found distributed practice effects are among the largest in cognitive psychology (d ≈ 0.4–0.6). Retention intervals that scale with the exam distance are optimal.

**How the planner applies it:**
- Each subject/topic appears on multiple non-consecutive days
- Topics studied early in the schedule reappear later as review
- The gap between sessions increases over time (expanding retrieval)

### 2. Interleaving

**Principle:** Mixing different topics or problem types within a single study session improves problem-solving and transfer, compared to blocking (studying one topic exhaustively before moving to the next).

**Key finding:** Rohrer & Taylor (2007) showed that interleaved practice produced far better performance on delayed tests (d ≈ 0.7), even though it feels harder during practice.

**How the planner applies it:**
- If multiple subjects are scheduled for a day, they are interleaved in 25–50 minute blocks
- Blocks alternate between subjects to maximize contrast
- The last block of each day reviews material from earlier blocks

### 3. Deliberate Rest and the Pomodoro Rhythm

**Principle:** Attention and cognitive performance degrade after ~50 minutes of continuous work. Short breaks restore focus.

**How the planner applies it:**
- Study blocks are 50 minutes with 10-minute breaks
- Lunch break of 60 minutes is scheduled mid-day
- The planner enforces a hard stop 8 hours before the next day's start (sleep protection)

### 4. Buffer Days

**Principle:** Plans without slack are fragile. The last 48 hours before an exam should be review-only, not new material.

**How the planner applies it:**
- The final 2 days of any plan are reserved for mixed review and practice tests
- No new topics are introduced in the buffer period
- This reduces pre-exam anxiety (you've seen it all before)

### 5. Topic Prioritization

When subjects have many sub-topics, the planner distributes them by difficulty:
- **Hard topics** are scheduled earlier in the plan (more time to absorb)
- **Medium topics** are interleaved in the middle
- **Easy topics** serve as warm-up or cooldown material

## Sample Schedule Output

For `--subjects "Calculus,History,Biology" --days 14 --hours-per-day 3`:

```json
{
  "exam_date": "2026-09-15",
  "total_study_days": 12,
  "buffer_days": 2,
  "schedule": [
    {
      "date": "2026-09-01",
      "blocks": [
        {"time": "09:00", "duration_min": 50, "subject": "Calculus", "topic": "Limits", "type": "new"},
        {"time": "10:00", "duration_min": 50, "subject": "History", "topic": "WWII Causes", "type": "new"},
        {"time": "11:10", "duration_min": 50, "subject": "Biology", "topic": "Cell Division", "type": "new"}
      ]
    }
  ]
}
```

## Limitations and Honest Caveats

- The planner does **not** know your prior mastery of each topic. It assumes equal starting knowledge. Adjust manually based on self-assessment.
- The planner assumes you follow the schedule. Real life has interruptions — use the buffer days as shock absorbers.
- Cognitive science principles are general; individual variation is real. If interleaving feels too chaotic, switch to longer blocks.

## References

1. Cepeda, N. J., Pashler, H., Mulik, E., Wixted, J. T., & Rohrer, D. (2006). "Distributed practice in verbal recall tasks: A review and quantitative synthesis." *Psychological Bulletin*, 132(3), 354–380.
2. Rohrer, D., & Taylor, K. (2007). "The shuffling of mathematics problems improves learning." *Instructional Science*, 35, 481–498.
3. Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). "Improving students' learning with effective learning techniques." *Psychological Science in the Public Interest*, 14(1), 4–58.
4. Bjork, R. A., & Bjork, E. L. (2011). "Making things hard on yourself, but in a good way: Desirable difficulties." *Successful Remembering and Successful Forgetting*, 323–346.
