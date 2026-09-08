## Description:

YuanCe guides agents through authorization-first web security testing on permitted targets, with Scope Guard checks, audit logging, and Markdown or JSON reporting without executable payload output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External developers, security engineers, and authorized testers use this skill to plan and document web security assessments for owned assets, bug-bounty scope, CTFs, and local training labs. It helps maintain authorization boundaries, produce vulnerability assessment reports, and preserve audit trails for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can be misapplied to targets outside an authorized testing scope.

Mitigation: Use the authorization-first Scope Guard workflow and test only assets owned by the user or explicitly permitted by a platform or written authorization.

Risk: Local scope and audit files may contain target names and testing actions.

Mitigation: Store scope and audit records in access-controlled workspaces and review or redact them before sharing exports or reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-testing)
- [YuanCe tutorial](references/tutorial.md)
- [Report template](references/report-template.md)
- [Four-stage methodology playbook](playbooks/00-methodology.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-security-testing)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration, shell commands, code]

**Output Format:** [Markdown guidance with shell commands and optional Markdown or JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope checks and audit logs are local; report generation redacts sensitive credentials.]

## Skill Version(s):

0.2.5 (source: server release evidence; artifact frontmatter, package.json, and changelog report 0.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
