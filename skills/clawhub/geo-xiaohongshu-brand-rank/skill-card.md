## Description:

Check whether Xiaohongshu AI search recommends a brand, where it ranks, which competitors appear, and which sites are cited, then create a shareable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hclscut](https://clawhub.ai/user/hclscut)

### License/Terms of Use:

MIT-0

## Use Case:

External brand and marketing teams use this skill to check how Xiaohongshu AI search presents their brand and competitors, review cited sources, and identify practical visibility improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags a scope and privacy concern: questions may be sent to AI platforms beyond the stated Xiaohongshu use, and external queries may incur credits.

Mitigation: Use the documented Xiaohongshu workflow, check the destinations and credit cost before running it, and do not include confidential information in prompts.

Risk: The setup flow asks for an API key in conversation, which could expose account access or credits.

Mitigation: Avoid sharing secrets in chat; revoke or rotate a key if it has been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hclscut/skills/geo-xiaohongshu-brand-rank)
- [MaxAEO Developer API documentation](https://maxaeo.cn/docs/developers/)
- [MaxAEO developer console](https://maxaeo.cn/developers/?utm_source=clawhub&utm_medium=skill)

## Skill Output:

**Output Type(s):** [Text, Guidance, HTML report]

**Output Format:** [Concise findings and recommendations with a shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings reflect the specific questions and responses collected in a run.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
