## Description:

Checks Doubao's recommendations for a brand, its position, competing brands, and cited pages, then creates a shareable HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hclscut](https://clawhub.ai/user/hclscut)

### License/Terms of Use:

MIT-0

## Use Case:

External brand and marketing teams use the skill to check how Doubao responds to product recommendation questions, compare the brands and cited sources in those answers, and get practical visibility guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's setup flow asks users to paste an API key into chat, which could expose the credential.

Mitigation: Do not send the key in chat; use a private credential setup method and replace a key that has already been shared.

Risk: Brand counts and ordering from a small number of AI answers may be mistaken for stable or verified recommendation rankings.

Mitigation: Present them as results from the specific questions and run, not as verified rankings or general mention rates.

## Reference(s):

- [MaxAEO developer documentation](https://maxaeo.cn/docs/developers/)
- [ClawHub skill release](https://clawhub.ai/hclscut/skills/geo-doubao-brand-rank)

## Skill Output:

**Output Type(s):** [Analysis, HTML report, Guidance]

**Output Format:** [Shareable HTML report with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes brand mentions and ordering in the queried answers, cited websites, and practical visibility suggestions. Results vary by question and run.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
