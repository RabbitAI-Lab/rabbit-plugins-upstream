## Description: <br>
Generates a warm, compact daily briefing with weather, calendar, reminders, birthdays, and important emails for cron or chat delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antgly](https://clawhub.ai/user/antgly) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Individuals using ClawHub or OpenClaw agents use this skill to generate a personal daily briefing from weather, calendar, reminders, birthdays, and optionally important emails for interactive use or scheduled cron delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive local data including email, contacts, calendar events, reminders, and birthdays. <br>
Mitigation: Install only if that access is acceptable, grant the minimum macOS permissions needed, and keep unused integrations disabled. <br>
Risk: The optional email feature may rely on an iCloud mailbox password stored in plain JSON configuration. <br>
Mitigation: Keep email analysis disabled unless needed, use an app-specific password, avoid shared plaintext configs, and rotate the password if exposed. <br>
Risk: The gathered briefing data is published to a predictable temporary file path. <br>
Mitigation: Run cleanup after use and prefer versions that use a private per-user storage path and delete generated data promptly. <br>
Risk: Configuration values and shell command inputs may affect local command execution. <br>
Mitigation: Review configuration before use and prefer versions that sanitize shell command inputs before invoking local tools. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/antgly/skills/daily-briefing) <br>
- [Apple app-specific password support](https://support.apple.com/en-us/HT204397) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text briefing with optional Markdown section labels and bullets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The briefing is generated from gathered local data and is intended to be short enough for chat or cron delivery.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
