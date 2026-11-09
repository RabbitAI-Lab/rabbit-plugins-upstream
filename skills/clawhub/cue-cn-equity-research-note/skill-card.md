## Description:

为未出财报期的个股研究整理七节逐条挂源的研究初稿，并将判断留给人工复核。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

投资研究人员可用此技能整理未出财报期的多来源个股研究初稿。它按业务、竞争、驱动因素和风险等七节组织材料，为每条发现附来源编号与检索日期，并把结论判断留待人工复核。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When CUE_API_KEY is configured, the workflow may send that credential to a destination selected from a remote catalog; the security scan is partial.

Mitigation: Leave the key unset for offline or user-supplied-material workflows. Before enabling remote retrieval, review the selected destination and provide only a credential intended for that service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-equity-research-note)
- [CUE data MCP configuration](https://cuecue.cn/hub/mcp)
- [CUE Omni Reader configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [七节 Markdown 个股研究初稿，发现项附来源编号，来源行含 URL 与检索日期]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [判断留待人工；不生成评级、目标价或买卖建议。]

## Skill Version(s):

0.1.0 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
