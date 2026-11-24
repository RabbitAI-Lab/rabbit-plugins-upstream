## Description:

Ask Qwen whether it recommends a brand, where it ranks, which competitors appear, and which pages it cites, then create a shareable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hclscut](https://clawhub.ai/user/hclscut)

### License/Terms of Use:

MIT-0

## Use Case:

Brand owners and marketers use this skill to check whether Qwen recommends a brand, compare its position with competitors, and review cited pages. They use the findings to guide Qwen visibility improvements and share an HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags credential handling as needing clarification.

Mitigation: Clarify API key storage and handling with MaxAEO before installing or entering a key.

Risk: ClawScan flags broad Qwen triggers and multi-platform paid queries.

Mitigation: Confirm the intended activation scope, platform coverage, and charges before running queries.

Risk: ClawScan reports an unexpected input-file overwrite.

Mitigation: Resolve and verify the reported overwrite behavior before use.

## Reference(s):

- [MaxAEO Developer API Documentation](https://maxaeo.cn/docs/developers/)
- [ClawHub Skill Release](https://clawhub.ai/hclscut/skills/geo-qianwen-brand-rank)

## Skill Output:

**Output Type(s):** [Analysis, Text, HTML report, Guidance]

**Output Format:** [Concise text and a shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report summarizes brand recommendations, rankings, competitors, and cited websites from the queried answers.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
