## Description:

AI KEY·标题与封面 helps agents produce multi-platform Chinese titles and cover text by matching title structures to the content, checking redlines, and explaining why each candidate fits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to generate platform-specific title and cover-text candidates, evaluate them against structure and redline criteria, and understand the tradeoffs behind each option.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read AI KEY reference or vault files and may save title feedback or performance notes locally.

Mitigation: Review configured memory and vault paths before use, and disable or audit persistence if local style preferences should not be retained.

Risk: Generated title guidance can be misleading if treated as a universal formula rather than checked against the user's own content and data.

Mitigation: Review candidates against the provided structure rationale, platform constraints, redline checks, and any available account-specific performance data before publication.

## Reference(s):

- [标题结构库](references/标题结构库.md)
- [规则卡](references/规则卡.md)
- [ClawHub Skill Page](https://clawhub.ai/iamzifei/skills/aikey-title)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured sections, title candidates, cover-text options, structure labels, and redline notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include title structure identifiers, platform constraints, rationale for each candidate, and recommendations for narrowing to preferred options.]

## Skill Version(s):

0.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
