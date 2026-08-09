## Description: <br>
Helps agents manage and synchronize Google Calendar, Microsoft Outlook, and Exchange calendar events with attention to account access and event changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and automation workflow users can use this skill to coordinate calendar access, cross-platform synchronization, meeting scheduling, and calendar event operations. It is not suitable for offline planning without calendar API access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar accounts and events could be affected by broad API scopes or insufficient confirmation before create, modify, delete, share, or sync actions. <br>
Mitigation: Use least-privilege calendar scopes, keep credentials out of version control, and require explicit user confirmation before any write, delete, sharing, or cross-platform sync operation. <br>
Risk: The artifact documentation is broad and internally inconsistent, which can make safeguards for calendar changes unclear. <br>
Mitigation: Review the skill before deployment and define local approval, logging, and rollback procedures for event-changing workflows. <br>


## Reference(s): <br>
- [Calendar Skill on ClawHub](https://clawhub.ai/thcjp/skills/calendar-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, JSON] <br>
**Output Format:** [Markdown instructions with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires calendar provider access and explicit handling of account credentials, API scopes, and event write operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
