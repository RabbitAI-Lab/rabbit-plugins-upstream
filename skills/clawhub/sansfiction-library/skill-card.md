## Description: <br>
Authorized SansFiction library manager that adds books, updates reading status, logs progress, and can schedule a daily reading check-in with a SansFiction personal token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fgbytes](https://clawhub.ai/user/fgbytes) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Readers and developers use this skill to manage a SansFiction library through an authorized account token, including adding books, updating reading status, logging progress, viewing current reads, and enabling a daily check-in. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a SansFiction read/write account token. <br>
Mitigation: Configure the token through secure OpenClaw settings or an environment variable when possible, avoid pasting it into chat, and rotate it if exposed. <br>
Risk: The skill can update library entries, reading status, and reading progress. <br>
Mitigation: Confirm the target book before making changes when a request is ambiguous or returns multiple plausible matches. <br>
Risk: The skill can create a recurring daily reading check-in. <br>
Mitigation: Explicitly confirm the reminder time and timezone before enabling the check-in. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fgbytes/skills/sansfiction-library) <br>
- [SansFiction](https://sansfiction.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call SansFiction MCP tools with a user-provided read/write token and may propose an OpenClaw cron reminder when requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
