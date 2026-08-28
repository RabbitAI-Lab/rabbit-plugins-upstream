## Description:

YuanCe (元测 yotta-security-testing) guides agents through authorization-first web security testing for in-scope assets using Scope Guard, vulnerability playbooks, report generation, and audit logging without executable payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security engineers, and authorized assessors use this skill to structure web security testing for self-owned assets, bug bounty scope, CTFs, and local labs. It helps agents check scope, follow vulnerability playbooks, generate Markdown or JSON reports, and keep an audit trail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports security testing workflows that could be misused outside authorized scope.

Mitigation: Keep scope.json limited to targets the user is actually allowed to test and require Scope Guard checks before target activity.

Risk: Local audit logs may contain target names and testing metadata.

Mitigation: Treat ~/.yottasec/audit.log as sensitive local assessment data and review exported logs before sharing.

Risk: Security reports may include sensitive evidence from findings data.

Mitigation: Use the built-in redaction behavior, minimize evidence, and manually review reports before submitting them to a bug bounty, SRC, or internal process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-testing)
- [Methodology playbook](playbooks/00-methodology.md)
- [Tutorial](references/tutorial.md)
- [Report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands; generated reports can be Markdown or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses scope.json for authorization state, writes local audit.log entries, and redacts sensitive values during report generation.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, CHANGELOG v0.1.0 dated 2026-08-29, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
