## Description:

Scans agent skills, MCP settings, tool permissions, and data access patterns for hardening opportunities, then produces a report and defensive guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use it to review agent environments they own or are authorized to assess, identify hardening opportunities across prompt injection, tool boundaries, and data isolation, and produce reports and defensive guardrails. It provides static configuration review and does not replace runtime controls or human security review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags installation behavior that can delete files through linked folders.

Mitigation: Review the local files in an isolated directory, avoid linked scan or installation folders, and back up existing installations before updating.

Risk: Reports may claim protection for checks that were skipped.

Mitigation: Select all three scan domains when evaluating this version.

Risk: Audit logs retain scan target paths, and generated guardrails require deliberate adoption.

Mitigation: Review access to audit logs and explicitly assess guardrails before adopting them.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-agent-hardening)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, Configuration]

**Output Format:** [Text, JSON, and Markdown reports; Markdown defensive guardrails and JSONL audit logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scans are read-only; audit logs and requested reports are written to disk. Guardrails are written only when requested.]

## Skill Version(s):

0.2.8 (source: SKILL.md frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
