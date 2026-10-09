## Description:

Guides authorization-first web security testing through reconnaissance, discovery, verification, and reporting, with scope checks and audit logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security practitioners and developers use this skill to plan and document web vulnerability assessments on explicitly authorized assets, bug-bounty targets, or training labs. It provides scope controls, testing playbooks, and report guidance rather than automated exploitation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security testing outside the owner's authorization may affect third-party systems.

Mitigation: Confirm written or platform authorization, register the exact permitted scope, and check each target and changed action before testing; do not conduct active testing on unapproved public targets.

Risk: Local scope records, audit logs, and vulnerability reports may contain sensitive target details.

Mitigation: Restrict access to local records, review generated reports before sharing, and keep only the minimum evidence needed.

Risk: Running an unpinned installer may install a different release or place files in unintended agent directories.

Mitigation: Pin the npm version, preview installation with --dry-run, choose the destination with --agent or --dir, and avoid global installation unless intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-security-testing)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-security-testing)
- [Tutorial](references/tutorial.md)
- [Report template](references/report-template.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Text guidance and Markdown or JSON vulnerability reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope decisions and local audit records; report generation redacts sensitive credentials.]

## Skill Version(s):

0.3.2 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
