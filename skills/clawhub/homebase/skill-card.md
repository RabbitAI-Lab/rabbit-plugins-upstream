## Description: <br>
Homebase is an OpenClaw household coordinator that helps families manage calendars, morning briefings, school email intake, groceries, meals, restaurant notes, medication logs, trip preparation, and optional fitness booking watchlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hchawla](https://clawhub.ai/user/hchawla) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Families and household operators use this skill through OpenClaw to coordinate daily logistics across Google Calendar, Gmail, WhatsApp, local household state files, and scheduled routines. It is intended for configured family environments where the user has reviewed the data access and automation settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access private family calendar and Gmail data and post information to configured WhatsApp chats. <br>
Mitigation: Install only after reviewing Google OAuth access, configured senders, family allowlists, and WhatsApp group IDs; use a dedicated Google project or account scope where practical. <br>
Risk: Scheduled automation can change calendar entries or send private household information without a same-turn manual review. <br>
Mitigation: Review cron jobs, Calendar delete behavior, and tool confirmations before enabling scheduled tasks; start with noncritical calendars or dry-run checks where available. <br>
Risk: The shared cron-health digest and optional Club Studio module add extra visibility or third-party automation exposure. <br>
Mitigation: Review shared cron log access before enabling owner digests, and leave Club Studio disabled unless browser automation against that third-party site is acceptable. <br>


## Reference(s): <br>
- [Homebase ClawHub skill page](https://clawhub.ai/hchawla/skills/homebase) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text guidance with JSON-oriented tool data and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update local JSON state through OpenClaw tool calls when configured.] <br>

## Skill Version(s): <br>
0.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
