## Description: <br>
The Primer helps an agent set up and maintain a personal coaching protocol that adapts to the user's life stage, growth goals, accountability needs, and preferred level of challenge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brucko](https://clawhub.ai/user/brucko) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to configure an agent as a personal development tutor that creates a PRIMER.md profile, tracks growth goals and patterns, and supports recurring reflection and accountability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persistently change future agent behavior through a personal coaching profile. <br>
Mitigation: Install only when the user intentionally wants persistent coaching behavior, and review the generated PRIMER.md before relying on it. <br>
Risk: The setup flow may update AGENTS.md and SOUL.md, which can affect future sessions. <br>
Mitigation: Review the exact AGENTS.md and SOUL.md edits before accepting them, and keep the changes narrow to Primer startup and role guidance. <br>
Risk: Recurring reflection or Miranda check-in automation may be scheduled without enough separate user control. <br>
Mitigation: Decline or manually manage cron reminders unless recurring automation is explicitly desired. <br>
Risk: Personal reflections and accountability notes may be stored in workspace files. <br>
Mitigation: Decide what reflections should be stored, retained, or deleted before setup and during later reviews. <br>


## Reference(s): <br>
- [Primer Template](assets/PRIMER-TEMPLATE.md) <br>
- [Life Stages Framework](references/life-stages.md) <br>
- [The Miranda Protocol](references/miranda-protocol.md) <br>
- [Primer Permissions](references/permissions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update PRIMER.md, AGENTS.md, SOUL.md, memory logs, and scheduled reminders.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
