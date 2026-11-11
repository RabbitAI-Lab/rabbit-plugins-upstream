## Description:

A股股东回报全景卡：把分红派息、回购注销、股东减持、股份质押这组股东行为公告拆成八项逐字卡，每项挂公告原句与锚，缺的进缺数清单，判断留人工。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要整理 A 股股东行为公告的读者，逐项摘录分红、回购、减持和质押信息及其原文锚点，列出缺失信息，并把投资判断留给人工。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports scanner concerns about retrieval of an unrelated remote catalog, privacy, and checker completeness; the scan is partial because a referenced path was missing.

Mitigation: Before installation, understand the remote catalog behavior and the external parser's data handling. Avoid sending private files, sensitive URLs, or credentials, and do not rely on the checker alone to confirm card completeness.

## Reference(s):

- [股东回报术语参考](references/sh-return-terms.md)
- [CUE Data MCP Catalog](https://cuecue.cn/api/mcp-catalog)
- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-cn-shareholder-return)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown with five sections and eight verbatim item cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records filing text with source anchors, lists missing fields, and leaves investment judgments to a human.]

## Skill Version(s):

0.1.1 (source: evidence release, frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
