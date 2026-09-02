## Description:

YuanCe yotta-security-testing is an authorization-first web security testing methodology that helps agents scope, assess, verify, and report findings only for approved targets, with Scope Guard, audit logging, and no executable payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security engineers, and authorized testers use this skill to guide web security testing for self-owned assets, approved bug-bounty scope, CTFs, and local labs. It supports scoping, audit logging, methodology playbooks, and Markdown or JSON vulnerability reports without providing executable payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be misapplied to targets outside the user's legal authorization.

Mitigation: Use it only for assets you are legally allowed to test and keep scope entries narrow in scope.json.

Risk: Local scope and audit files can record sensitive target and testing-process details.

Mitigation: Store ~/.yottasec files with appropriate local access controls and review them before sharing reports or logs.

Risk: Security-testing conclusions may be incomplete or need contextual judgment.

Mitigation: Treat generated findings and reports as drafts for qualified human review before action or submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-testing)
- [YuanCe tutorial](references/tutorial.md)
- [Report template](references/report-template.md)
- [Methodology playbook](playbooks/00-methodology.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, json, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands; generated reports may be Markdown or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local scope and audit files; generated reports redact sensitive credentials.]

## Skill Version(s):

0.2.4 (source: frontmatter, package.json, changelog, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
