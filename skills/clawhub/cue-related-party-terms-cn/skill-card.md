## Description:

将一份A股关联交易公告、预计公告或协议整理为八项带原文引句与来源定位的条款卡，并标出未检索到的信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

供分析师、法务及投研人员核对单笔A股关联交易披露中的交易身份、标的、定价与金额、结算和审议程序。公允性、审批结果和投资影响由人工判断。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious, citing remote MCP discovery that may not match its stated document-review purpose.

Mitigation: Review the remote MCP discovery examples before installing.

Risk: The scanner raises concerns about where the optional API key is sent and what external attachment parsing transmits.

Mitigation: Check the API key destination and the data sent for attachment parsing before providing credentials or documents.

Risk: The scanner flags unpinned installer and skill sources.

Mitigation: Use pinned installer and skill revisions.

Risk: The security scan was partial because a local reference was unresolved, so the available evidence is incomplete.

Mitigation: Review the unresolved reference and treat the security assessment as incomplete.

## Reference(s):

- [关联交易条款速查](references/rpt-terms.md)
- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-related-party-terms-cn)
- [CUE MCP setup](https://cuecue.cn/hub/mcp)
- [CUE Omni Reader setup](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with eight clause entries, verbatim quotations, source anchors, and missing-data notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes comparison and human-review sections; does not assess fairness, approval likelihood, or investment impact.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
