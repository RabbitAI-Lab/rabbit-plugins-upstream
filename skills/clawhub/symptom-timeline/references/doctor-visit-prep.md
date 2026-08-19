# Doctor Visit Preparation

How to present your symptom data effectively during medical appointments.

---

## Before the Visit

1. **Generate your report** at least a day before:
   ```bash
   python3 scripts/symptom_tracker.py export --output my_report.txt
   python3 scripts/symptom_tracker.py summary
   ```

2. **Review correlations** to understand your patterns:
   ```bash
   python3 scripts/symptom_tracker.py correlate
   ```

3. **Check for flare-ups** so you can discuss them:
   ```bash
   python3 scripts/symptom_tracker.py flare-up
   ```

4. **Highlight the top 3 issues** you want to discuss — doctors have limited time.

## During the Visit

### Lead with the summary, not the raw data
Doctors are time-pressed. Start with:
- "I've been tracking my symptoms for [X weeks]."
- "My top concern is [symptom] — it's been [trending up/stable/spiking]."
- "I've noticed it correlates with [trigger]."

### Bring the printed report
Hand over the exported text report. It provides:
- A clear timeline they can scan
- Objective severity data (not just "it's been bad")
- Identified triggers they can evaluate
- Medications you've taken (so they can check interactions)

### Key questions to ask
- "Does this pattern match what you'd expect for [condition]?"
- "Could any of these triggers be modified?"
- "Should I adjust my medication based on this data?"
- "Are there additional symptoms I should be tracking?"
- "Does the severity trend suggest we need to change the treatment plan?"

## What Doctors Look For

| Data Point | Why It Matters |
|-----------|----------------|
| **Frequency** | How often = severity of the condition |
| **Severity trend** | Worsening = treatment may need adjusting |
| **Triggers** | Avoidable triggers = actionable advice |
| **Response to medication** | Did severity drop after starting a med? |
| **Flare-up patterns** | Helps predict and prevent future episodes |
| **Co-occurring symptoms** | May indicate a unified underlying cause |

## Effective Communication Tips

1. **Be quantifiable** — "7 out of 10, three times this week" beats "it's been really bad."
2. **Show trends** — "It was a 5 last month, now it's an 8" is powerful information.
3. **Don't over-explain** — let the report speak; fill in context when asked.
4. **Mention medication changes** — if you started/stopped anything, flag it.
5. **Ask for a follow-up plan** — what to track next, when to come back.

## After the Visit

- Log any new diagnoses or medication changes as notes
- Add any new tracking recommendations from the doctor
- Continue logging to measure whether the new treatment plan is working
- Run `correlate` after 2-4 weeks to see if patterns have shifted
