# Demo Happy Path & Failure-Proofing

Required for every live demo. No demo enters the show without this filled out and signed off.

---

## Demo identity
- **Demo name:**
- **Slot in keynote:** [segment / beat / minute]
- **Speaker(s) on stage:**
- **Demo operator (off-stage):**
- **Demo engineer (built it):**
- **Target duration:** [stage time, not total interaction]

## The happy path (step by step)
Number every input. Be ruthlessly specific.

| Step | Speaker says | Operator does | What appears on screen | Expected duration |
|---|---|---|---|---|
| 1 | "Let's start with a simple ask..." | Types prompt: `[exact text]` | Cursor in input field | 5s |
| 2 | "Watch what happens..." | Hits enter | Model begins streaming response | 8s |
| 3 | [reads first line aloud] | (no action) | Response continues | 6s |
| ... |  |  |  |  |

## Reset state
- **What state must the system be in at minute 0?**
- **How is reset confirmed?** [checklist, screenshot diff, dry-run]
- **Reset script / runbook:**
- **Who runs the reset and when?**

## Dependencies
- **Network:** [caged / venue Wi-Fi / wired / cellular backup]
- **Backend services:** [list — each with a status owner]
- **Latency tolerance:** [what's acceptable; what's a trigger to abort]
- **Credentials in use:** [test account vs. prod; who controls]
- **Data privacy:** [is anything shown that needs scrubbing?]

## The "failure trigger" — when do we abort to backup?
- **Hard triggers (abort immediately):**
  - [e.g., model returns error]
  - [e.g., load time > 8 seconds]
  - [e.g., wrong screen visible]
- **Soft triggers (operator's call):**
  - [e.g., minor latency, recoverable in flow]

## Backup plan
- **Backup recording:** [filename, location on playback system, who can roll it]
- **Backup operator (failover):** [name, comms channel]
- **Speaker's bridge language if we cut to recording:**
  > "Let me show you what this looks like..." [pivot to recording without acknowledging failure]
- **What does the speaker say if both fail?**
  > "We're still putting the final polish on this — we'll share a video in the follow-up. The point is..."

## Rehearsal log
| Date | What was tested | Pass/Fail | Notes |
|---|---|---|---|
|  |  |  |  |

## Sign-offs (required before lock)
- ☐ Demo engineer signs off on happy path
- ☐ Demo operator signs off on operability
- ☐ Speaker has rehearsed the demo at least 3 times
- ☐ Backup recording exists and has been verified
- ☐ Failover operator briefed and on comms
- ☐ Reset script verified
- ☐ Producer signs off

## Producer's bet
**On a scale of 1–10, what's the producer's confidence this demo goes live without intervention?**

If < 7, plan to cut to recording by default and only go live if conditions are right.
