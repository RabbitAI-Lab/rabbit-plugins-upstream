## Description:

Scans selected documents, code, and logs for common sensitive strings and provides masked text with an optional findings report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Developers and other document publishers use this skill to check material before external sharing, mask likely personal information, secrets, internal paths, and project codenames, and review the findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional findings reports include partial samples of sensitive matches in terminal output.

Mitigation: Use only explicitly chosen input and avoid report output in CI, shared terminals, or logs containing real secrets.

Risk: Pattern-based masking may miss sensitive details or require judgment about what to redact.

Mitigation: Manually review the masked material and findings before external publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/doc-desens-scanner)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Masked text on standard output; optional JSON findings report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include partial match samples; review masked results before publication.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled SKILL.md says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
