## Description:

Scans documents, code, and logs for personal identifiers, credentials, internal paths, and project names, then provides masked text and an optional findings report before external sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and other people preparing documents, code, or logs for external sharing use this skill to find and mask potentially sensitive text and inspect a findings report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pattern-based masking may leave sensitive content in the output.

Mitigation: Review the sanitized copy manually before external release.

Risk: The --file option reads the path supplied by the user.

Mitigation: Provide only the intended file and control access to the scan output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/zz-pipeline-smoke)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Masked plain text with an optional JSON findings report on standard output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The optional report gives a finding count, categories, and abbreviated samples; results require review before external release.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
