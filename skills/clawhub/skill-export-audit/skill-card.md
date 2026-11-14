## Description:

Audits a local Hermes skill and its published registry version before export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blueboyzx](https://clawhub.ai/user/blueboyzx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when preparing or updating Hermes skills for ClawHub or another community registry. It guides accuracy, security, metadata, staging, and publish verification so the local and public versions can be corrected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running bundled scripts on real inputs may expose sensitive data or credentials, and the available security review is incomplete.

Mitigation: Inspect scripts before use, run them on sanitized copies in an isolated environment, and withhold credentials and broad system access.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/blueboyzx/skills/skill-export-audit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown audit guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and recommended steps vary with the audited skill.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
