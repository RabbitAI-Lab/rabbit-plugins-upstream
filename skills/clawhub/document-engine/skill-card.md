## Description:

Audits Chinese business documents offline with deterministic rules and produces scored findings and traceable reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance reviewers and developers use this skill to screen Chinese contracts, regulations, official documents, and other business documents for rule-based issues and generate audit reports for review or integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTML reports from untrusted documents may execute injected browser scripts because dynamic document content is not escaped.

Mitigation: Prefer JSON or Markdown output for untrusted documents; open HTML reports only from trusted inputs until dynamic fields are escaped and a restrictive CSP is added.

Risk: Unreviewed custom rule directories may produce misleading audit results.

Mitigation: Review custom rule files before using --rules-dir and verify important findings against the source document.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nohn3043-arch/skills/document-engine)
- [Project homepage (listed in skill metadata)](https://github.com/nohn3043-arch/Story-engine)
- [Rule catalog and custom rule format](references/RuleCatalog.md)
- [Usage guide](references/UsageGuide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML]

**Output Format:** [Chinese-language audit reports with scores, findings, and trace details; text verdicts on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally without network access; report timestamps and trace IDs vary between runs.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
