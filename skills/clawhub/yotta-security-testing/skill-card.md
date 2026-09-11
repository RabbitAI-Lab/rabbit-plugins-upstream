## Description:

元测 yotta-security-testing is a disciplined, authorization-first AI security-testing methodology for web security testing on authorized targets, covering reconnaissance, discovery, verification, and reporting with Scope Guard controls and no executable payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security practitioners, developers, and authorized bug-bounty or training participants use this skill to structure web vulnerability assessment, penetration-test reporting, scope checks, and audit logging for assets they are allowed to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist sensitive targets in local scope files, audit logs, or generated reports.

Mitigation: Avoid passwords, tokens, cookies, authenticated URLs, and sensitive scan metadata in targets or findings; review generated reports and logs before sharing.

Risk: The installer may add the skill broadly across user-level agent environments.

Mitigation: Install only in the agent environments where this security-testing workflow is intentionally needed.

Risk: Unpinned package installation can change the installed code over time.

Mitigation: Prefer a pinned package version when installing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-security-testing)
- [Tutorial](references/tutorial.md)
- [Report Template](references/report-template.md)
- [FAQ](references/faq.md)
- [Methodology Playbook](playbooks/00-methodology.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, text]

**Output Format:** [Markdown guidance with shell command examples, configuration files, JSON audit data, and Markdown or JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Scope Guard authorization checks and report redaction before producing testing records or reports.]

## Skill Version(s):

0.3.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
