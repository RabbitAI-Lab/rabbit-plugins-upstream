## Description:

Checks research manuscripts against their own numbers, citations, figures, reporting standards, and available code or data, then produces an evidence-backed review report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[biajin-pku](https://clawhub.ai/user/biajin-pku)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and reviewers use the skill to check a manuscript for numerical inconsistencies, unsupported claims, reference problems, reporting omissions, and discrepancies with available code or data before review or submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference lookups send and cache manuscript-derived reference metadata by default.

Mitigation: Use --offline for confidential manuscripts and handle generated reports and caches as sensitive material.

Risk: LaTeX includes and bibliography paths can read outside the selected manuscript directory.

Mitigation: Avoid untrusted LaTeX or Overleaf archives until their include and bibliography paths are confined to the manuscript directory.

Risk: Inspecting companion code or data may execute untrusted code.

Mitigation: Sandbox companion code and data before running checks that inspect them.

## Reference(s):

- [Paper Fact Check release](https://clawhub.ai/biajin-pku/skills/paperfactcheck)
- [Reading checklist](references/checklist.md)
- [Reporting guideline selector](references/guidelines/README.md)
- [Review format](references/review-format.md)

## Skill Output:

**Output Type(s):** [Markdown guidance, HTML report, JSON findings, Text]

**Output Format:** [HTML report and JSON findings with a brief Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings quote manuscript passages, show supporting arithmetic where relevant, suggest fixes, and distinguish unverified checks.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
