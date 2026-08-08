## Description:

Stellar Trails provides a six-phase agent workflow for coding, document creation, visualization, data processing, planning, and general task execution with traceability IDs, entry and exit gates, scope commitment, and delivery reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to impose a structured workflow around implementation, analysis, document, visualization, and planning tasks. It helps agents classify task complexity, plan and verify work, report scope drift, and preserve task continuity through structured summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill acts as an always-on workflow controller and runs shell commands during activation.

Mitigation: Install only when continuous workflow enforcement is desired, and review the activation steps before enabling it in a workspace.

Risk: The activation flow can start a persistent local HTTP server.

Mitigation: Disable the popup server or bind it to localhost unless the preview is required, and confirm exposed ports before use.

Risk: The skill can use a local GitHub PAT if present and configure Git credentials from it.

Mitigation: Remove or disable PAT automation for routine use, provide tokens only for explicit GitHub operations, and avoid logging token values.

Risk: The skill may update itself through ClawHub during activation.

Mitigation: Make updates manual for reviewed environments, and inspect version changes before accepting updated instructions.

Risk: The skill stores cross-session task, pattern, scenario, and user-profile data.

Mitigation: Review and redact stored worklog and knowledge files, or disable memory writes for sensitive projects.

## Reference(s):

- [Stellar Trails ClawHub release](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [AskUserQuestion Gate](references/askuserquestion-gate.md)
- [SADC Subagent Delegation](references/sadc-subagent-delegation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured scope and delivery reports, and file paths for produced artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task plans, verification summaries, traceability reports, generated files, configuration changes, and shell commands for the active workspace.]

## Skill Version(s):

9.11.3 (source: server release metadata and SKILL.md Metadata section)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
