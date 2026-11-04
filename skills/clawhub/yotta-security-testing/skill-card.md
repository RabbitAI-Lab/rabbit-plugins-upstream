## Description:

Guides agents through a four-stage web security assessment workflow for explicitly authorized targets, with scope checks, audit guidance, and report preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security engineers, developers, and authorized testers use this skill to plan and document web security assessments of assets they are permitted to test, including labs, CTFs, and approved bug-bounty scopes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authorization guard may allow paths outside the approved target scope.

Mitigation: Independently enforce exact authorized URL boundaries until the scope guard is corrected.

Risk: Credentials may remain in scan metadata, target URLs, reports, or audit exports.

Mitigation: Remove credentials from scan metadata and target URLs, then manually inspect reports and audit exports before sharing.

Risk: The security review did not cover downloaded npm releases or host permission enforcement.

Mitigation: Install reviewed bundled files or a verified exact package version into a deliberately selected directory.

## Reference(s):

- [Methodology and testing workflow](playbooks/00-methodology.md)
- [Security testing tutorial](references/tutorial.md)
- [Report template and findings schema](references/report-template.md)
- [Yotta Security Testing repository](https://github.com/YottaMeta/yotta-security-testing)
- [Yotta Security Testing on npm](https://www.npmjs.com/package/@yottameta/yotta-security-testing)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown and JSON report content, with plain-text guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report examples use redacted credentials and class-based verification descriptions; conclusions require human review.]

## Skill Version(s):

0.3.3 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
