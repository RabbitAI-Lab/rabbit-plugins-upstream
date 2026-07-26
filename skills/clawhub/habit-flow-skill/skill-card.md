## Description: <br>
AI-powered atomic habit tracker with natural language logging, streak tracking, smart reminders, and coaching. Use for creating habits, logging completions naturally ("I meditated today"), viewing progress, and getting personalized coaching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tralves](https://clawhub.ai/user/tralves) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use Habit Flow to create and manage habits, log completions in natural language, review streaks and completion statistics, configure reminders, and receive coaching. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Habit data is stored under ~/clawd/habit-flow-data. <br>
Mitigation: Install only if local storage of habit data is acceptable, and protect that directory according to the user's privacy needs. <br>
Risk: Reminder synchronization can turn habit names or reminder messages into shell commands. <br>
Mitigation: Do not sync reminders from untrusted habit names or reminder messages until shell command construction is fixed. <br>
Risk: Reminders and proactive coaching can create persistent outbound messaging paths to a chat channel. <br>
Mitigation: Review the exact notification destination before enabling reminders or proactive coaching. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tralves/skills/habit-flow-skill) <br>
- [Publisher profile](https://clawhub.ai/user/tralves) <br>
- [Commands reference](references/COMMANDS.md) <br>
- [Data storage reference](references/DATA.md) <br>
- [Reminder reference](references/REMINDERS.md) <br>
- [Proactive coaching reference](references/proactive-coaching.md) <br>
- [Data schema reference](references/data-schema.md) <br>
- [Coaching techniques reference](references/atomic-habits-coaching.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and generated habit data, statistics, and visualization files when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+ and npm; habit data is stored under ~/clawd/habit-flow-data.] <br>

## Skill Version(s): <br>
1.5.4 (source: frontmatter, package.json, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
