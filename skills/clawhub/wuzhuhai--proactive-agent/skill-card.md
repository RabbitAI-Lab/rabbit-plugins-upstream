## Description:

Transforms task-following agents into proactive partners that anticipate needs, preserve working memory, verify outcomes, and improve through guarded routines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuzhuhai](https://clawhub.ai/user/wuzhuhai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install a proactive operating pattern for AI agents, including onboarding, memory capture, heartbeat checks, reverse prompting, security checks, and guarded self-improvement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory capture may retain sensitive personal, project, or workspace information longer than intended.

Mitigation: Disable or narrow automatic memory capture, exclude secrets and sensitive identifiers, and periodically review retained memory files.

Risk: Updates to operating files such as AGENTS.md, TOOLS.md, or skill files can change future agent behavior.

Mitigation: Require human review before updating operating rules or skill instructions, and keep changes small enough to audit.

Risk: Heartbeat routines, scheduled prompts, and cleanup workflows may encourage autonomous action in areas that need user approval.

Mitigation: Treat scheduled crons, app or tab cleanup, deletion, external messages, posts, purchases, and other public or irreversible actions as opt-in and approval-gated.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wuzhuhai/skills/proactive-agent)
- [Publisher Profile](https://clawhub.ai/user/wuzhuhai)
- [Onboarding Flow Reference](artifact/references/onboarding-flow.md)
- [Security Patterns Reference](artifact/references/security-patterns.md)
- [Source Author Profile](https://x.com/halthelobster)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and starter configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional workspace memory files and a security audit shell script.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter states 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
