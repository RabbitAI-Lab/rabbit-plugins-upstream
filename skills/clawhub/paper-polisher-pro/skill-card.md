## Description:

Helps authors review academic writing for AI-writing signals, terminology consistency, style, and disclosure needs using local analysis tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and editors use this skill to self-review Chinese or English academic manuscripts, identify passages needing attention, check terminology and AI-use disclosures, and plan revisions before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detector-focused revision guidance could be used to conceal AI authorship.

Mitigation: Use reports for author self-review and disclosure; do not use fingerprint or de-AI guidance to misrepresent AI-generated work as human-written.

Risk: Write-capable commands can change manuscripts or local evaluation data.

Mitigation: Run auto-fix, apply, freshness-refresh, and corpus-building commands only on files and datasets you are authorized to modify or copy.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands]

**Output Format:** [Markdown guidance and command examples; local tools can produce JSON, text, and HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AI-risk scores are advisory; texts under 100 characters receive no risk verdict.]

## Skill Version(s):

3.9.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
