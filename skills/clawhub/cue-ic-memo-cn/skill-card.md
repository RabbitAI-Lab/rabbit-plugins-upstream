## Description:

起草中文投决备忘录讨论稿，为事实与数字附上可回查出处和定位，并明确标出缺失信息与多空观点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

投资研究人员与投前团队可将公司材料整理为中文七节投决讨论稿，逐条列出来源与定位、缺失信息及多空观点，供人工核验和内部讨论；不用于投资建议或决策。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection setup may expose the API key.

Mitigation: Use the local drafting path until destination checks protect both the shell example and redirects.

Risk: Evidence checks may miss unsupported claims.

Mitigation: Independently verify citations even when a checker reports PASS.

Risk: Confidential documents may undergo external processing.

Mitigation: Explicitly approve any external processing of confidential documents.

Risk: Unreviewed or unpinned versions may be installed.

Mitigation: Install reviewed, pinned versions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huhoo/skills/cue-ic-memo-cn)
- [CUE MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL]

**Output Format:** [Chinese seven-section Markdown memo with an accompanying JSON run account and JSONL source index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft for human review; citations require independent verification, and unavailable facts are labeled rather than inferred.]

## Skill Version(s):

0.3.2 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
