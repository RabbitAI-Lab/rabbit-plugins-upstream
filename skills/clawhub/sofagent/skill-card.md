## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI adoption by constraining agent behavior, auditing changes, preserving lessons learned, and maintaining an optimization workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise deployment engineers and agent operators use this skill to structure FDE discovery, quantify automation opportunities, build enterprise-specific skill guidance, and run audit-oriented handoff and sustainment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents broad persistent control over agent behavior, local configuration, shell delegation, hooks, and background automation.

Mitigation: Install and test only in a controlled enterprise environment after reviewing installer source, pinning packages, and defining a clear uninstall plan.

Risk: Documented install, npx, and shell-delegation commands could be risky if run with untrusted task text or production credentials.

Mitigation: Require explicit approval for each config write, hook, daemon, webhook, or shell action, and avoid production credentials until controls are verified.

Risk: The artifact describes automated auditing, rollback, MCP tooling, and sustainment workflows that may affect local agent operation.

Mitigation: Review the active configuration and tool permissions before enabling MCP, daemon, audit, or rollback workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Publisher profile](https://clawhub.ai/user/kongfangxun)
- [Engineering minimal-change source template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Engineering code-reviewer source template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce audit reports, deployment guidance, handoff notes, workflow descriptions, and configuration instructions.]

## Skill Version(s):

1.4.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
