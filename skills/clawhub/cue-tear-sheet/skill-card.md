## Description:

根据公开披露为指定公司整理一页速览，涵盖身份、近四期财务、符合日期条件的事件和直查风险，并保留观点栏供人工填写。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

供投研人员在会前或准备客户简报时快速整理单家公司的披露事实。每项数据带来源锚，观点由人工填写；不用于深度尽调或投资建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional Cue setup can send an API key to a catalog-selected address without checking its security or ownership.

Mitigation: Use the user-supplied disclosure path until destinations are restricted to verified Cue HTTPS endpoints. Keep keys out of chat, and review and pin the installer and skill revision.

Risk: The page validator may miss issues in report opinions and source links.

Mitigation: Manually review report opinions and source links.

## Reference(s):

- [Cue data channel setup](https://cuecue.cn/hub/mcp)
- [Cue document parsing setup](https://cuecue.cn/hub/omni-reader)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, JSONL, Text]

**Output Format:** [Markdown tear sheet and progress log with a JSONL source index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For up to five companies; the three-line opinion section is left for a human.]

## Skill Version(s):

0.1.20 (source: frontmatter; server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
