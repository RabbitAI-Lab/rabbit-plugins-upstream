## Description:

品牌进入品类、推出新品或重做内容策略之前，通过公开内容（笔记、达人主页、评论）看清用户问题、内容回答、达人可信度、用户信任和供给饱和度，形成带证据边界的品牌建议与 GO/NO-GO 决策结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qomob](https://clawhub.ai/user/qomob)

### License/Terms of Use:

MIT-0

## Use Case:

品牌策略、内容和增长团队使用该技能对小红书品类或赛道做公开内容抽样分析，识别用户关切、内容供给、达人可信边界和进入风险。交付物支持新品进入、内容策略重做或赛道 GO/NO-GO 投决。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collected public posts or comments may contain personal identifiers or sensitive user context.

Mitigation: Use only public data, keep collection small and rate-limited, and remove nicknames or other personal identifiers from outputs.

Risk: Optional collectors and integrations can interact with Xiaohongshu or third-party APIs under user-controlled accounts.

Mitigation: Run collection only with an authorized account and review optional external Agent-Reach or third-party API setup separately before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qomob/skills/xhs-track-analysis)
- [Methodology](references/methodology.md)
- [Data sources](references/data-sources.md)
- [Collection playbook](references/collection-playbook.md)
- [Table template](references/table-template.md)
- [Case study](references/case-study.md)

## Skill Output:

**Output Type(s):** [markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown analysis tables and decision brief with optional shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes evidence boundaries, GO/NO-GO decision posture, and optional script-driven completeness checks.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
