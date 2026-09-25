## Description:

Configures and audits server and cloud firewall rules to manage access, block risky traffic, and report rule or configuration issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and security operators use this skill to request firewall rule configuration, cloud firewall management, rule audits, and risk-oriented firewall guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firewall rule changes can disrupt access or expose services when scope, confirmation, backup, and rollback steps are missing.

Mitigation: Use the skill only with explicit target hosts, ports, actions, and rollback plans; prefer audit or dry-run review before applying changes.

Risk: The skill requests command and write authority for high-impact firewall work.

Mitigation: Run it in a tightly supervised session with least privilege and require human approval before executing commands or writing configuration.

Risk: Firewall behavior varies by operating system, cloud provider, and rule ordering.

Mitigation: Verify platform-specific commands and test proposed rules in a non-production or maintenance-window workflow before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/firewall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON summaries and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include firewall rule proposals, audit findings, risk notes, and command snippets.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
