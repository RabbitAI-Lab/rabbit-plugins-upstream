## Description: <br>
Give your AI agent access to your health and fitness data from RUNSTR, including workouts, habits, journal entries, mood, steps, and related Nostr-backed records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thewildhustle](https://clawhub.ai/user/thewildhustle) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use this skill to retrieve RUNSTR fitness backups from Nostr, decrypt personal health records, summarize activity, analyze habits and mood, and provide fitness coaching based on the user's own data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks the user to provide a full Nostr private key for RUNSTR data access. <br>
Mitigation: Use a dedicated RUNSTR or Nostr identity, avoid a primary nsec, and keep the key out of reusable chat contexts, logs, and command arguments where possible. <br>
Risk: The skill accesses sensitive health, fitness, mood, habit, journal, and step data. <br>
Mitigation: Share only the data needed for the task and review outputs before storing, forwarding, or relying on health-related summaries. <br>
Risk: The artifact suggests saving a structured health summary for future conversations. <br>
Mitigation: Store summaries only with explicit user consent and avoid retaining private health details longer than needed. <br>


## Reference(s): <br>
- [RUNSTR website](https://runstr.app) <br>
- [RUNSTR GitHub organization](https://github.com/RUNSTR) <br>
- [nak install package](https://github.com/fiatjaf/nak) <br>
- [ClawHub skill page](https://clawhub.ai/thewildhustle/skills/runstr-fitness) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Markdown, Analysis, Guidance] <br>
**Output Format:** [Markdown with shell commands, JSON payloads, and structured health summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query Nostr relays, decrypt RUNSTR backup data, and propose stored health summaries for future conversations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
