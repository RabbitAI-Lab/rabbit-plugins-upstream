## Description:

Helps agents draft and refine Chinese social-media titles and cover text by matching the content shape to title structures, checking red-line rules, and explaining each recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to generate and refine platform-specific titles, cover text, descriptions, and topic tags for Chinese social content while preserving audience, platform, structure, and red-line checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read shared vault guidance and memory, then save feedback or performance notes for future use.

Mitigation: Use an isolated workspace or vault, review generated memory records, and avoid providing sensitive or cross-user feedback unless inspection and deletion controls are available.

Risk: Generated titles and cover text can still contain inaccurate claims, unsuitable framing, or platform-policy issues despite built-in red-line checks.

Mitigation: Review recommendations before publication for factual accuracy, brand fit, platform rules, and local legal requirements.

## Reference(s):

- [标题结构库](references/标题结构库.md)
- [规则卡](references/规则卡.md)
- [ClawHub release page](https://clawhub.ai/iamzifei/skills/zmm-title)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured candidate sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language copywriting output with title structure IDs, platform constraints, red-line status, shortlist rationale, and optional cover text or opening-line revision.]

## Skill Version(s):

0.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
