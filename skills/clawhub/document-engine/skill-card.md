## Description:

Audits Chinese business documents against deterministic rules and produces findings, scores, and traceable reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance teams and developers use this skill to screen Chinese contracts, regulations, and official documents for rule-based issues and export reviewable audit reports. Findings are screening results, not a substitute for expert review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTML reports may execute content embedded in untrusted documents or custom rule files when opened in a browser.

Mitigation: Use JSON or Markdown for untrusted inputs; only open HTML reports from trusted documents and rule files until output is safely escaped.

Risk: Custom rule messages and patterns can alter report findings and content.

Mitigation: Review custom rule directories before using them for an audit.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nohn3043-arch/skills/document-engine)
- [Project homepage listed in metadata (source provenance unavailable)](https://github.com/nohn3043-arch/Story-engine)
- [Rule catalog](references/RuleCatalog.md)
- [Usage guide](references/UsageGuide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML]

**Output Format:** [Document audit reports in HTML, JSON, or Markdown, with a text summary on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a score, pass/fail result, findings with severity and suggested fixes, and an audit trace.]

## Skill Version(s):

1.0.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
