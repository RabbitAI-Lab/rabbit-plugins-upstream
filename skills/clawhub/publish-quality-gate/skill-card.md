## Description:

发布质量门禁 helps agents check Skills, expert packages, documents, and tools before and after external release by running four layers of sensitive-information review and a TRACE self-assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, maintainers, and release reviewers use this skill to check external release candidates for sensitive company, local-machine, personal, and confidential information, then document post-release quality using the TRACE dimensions. It is intended for publishing workflows where an agent should produce review guidance, scanner commands, and a structured Markdown assessment report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner output can expose real secrets, personal data, or sensitive file paths when findings are printed to a terminal or CI log.

Mitigation: Run scans only on artifacts you choose in a private terminal, avoid publishing raw logs, and redact sensitive matches before sharing results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/publish-quality-gate)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Overview Diagram](assets/overview.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown checklists, report templates, scanner commands, and terminal scan summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local scanner reports suspected sensitive matches and relies on human review to distinguish real findings from false positives.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
