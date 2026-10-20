## Description:

Helps authors review academic drafts for AI-like writing patterns, terminology and style consistency, and disclosure-related issues, with sentence-level polishing guidance rather than automatic rewrites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors and editors use this skill to self-check drafts, inspect potential AI-writing signals, and improve clarity and consistency while observing their institution's AI disclosure rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-rate lowering and rewrite-comparison workflows could be used to tune writing around AI detectors.

Mitigation: Use findings for writing-quality review and disclosure compliance, not to conceal AI-generated work or evade institutional checks.

Risk: Batch or recursive scans may read sensitive local drafts and reports may expose their contents.

Mitigation: Limit scans to intended document directories and review generated reports before sharing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Best practices](references/best-practices.md)
- [Architecture and limitations](references/architecture.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Guidance]

**Output Format:** [Plain-language feedback and polishing guidance, structured JSON results, and optional HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers suggestions without rewriting drafts automatically; text under 100 characters receives no verdict.]

## Skill Version(s):

6.1.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
