## Description:

Data Minimizer masks phone numbers, email addresses, ID numbers, long numbers, and custom names before text is sent to an AI, and returns masked text plus a masking report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and other AI users use this skill to locally redact common personally identifiable information from text before sharing it with an AI system. It is intended as a helper step before external processing, with human review of the masked result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented global installer path may install an unpinned package.

Mitigation: Install only from a reviewed, pinned version or commit, and avoid running global installers from an elevated shell.

Risk: Automated masking can miss sensitive content outside the supported patterns.

Mitigation: Review the masked output before sending text to another AI service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/data-minimizer)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Plain text report or JSON with optional masked-text file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local deterministic redaction helper; supported matches include phone numbers, email addresses, ID numbers, long numbers, and user-supplied names.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
