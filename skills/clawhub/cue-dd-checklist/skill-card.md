## Description:

给一家 A 股公司拉一份公开信息风险清单：查得到的逐条带披露锚，查不到的逐类写明原因；不给投资结论，不出法律意见。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

投前初筛、授信背景核查或并购线索梳理人员可用它检查单一 A 股主体在指定日期和回看窗口内的公开披露。它整理带来源锚的风险事实与九类覆盖情况，结论留给人工判断。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Credential safeguards can be bypassed, and company-attribution checks are weaker than promised.

Mitigation: Prefer the user-supplied public-disclosure workflow without an API key until both credential paths validate destinations and redirects safely; check each fact against the original company record.

Risk: Optional services may process submitted material remotely, and optional dependencies and remaining fixture contents were not fully audited.

Mitigation: Confirm remote processing before supplying confidential files, and pin installer and source revisions.

## Reference(s):

- [ClawHub release](https://clawhub.ai/huhoo/skills/cue-dd-checklist)
- [Cue data MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader configuration](https://cuecue.cn/hub/omni-reader)
- [Coverage map template](references/coverage-map-template.md)
- [Channel map](references/channel-map.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, JSON Lines]

**Output Format:** [A dated Markdown report, JSON Lines source index, JSON evidence snapshots, coverage map and run log]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-subject, time-bounded draft with a fixed seven-column fact table and nine-category coverage ledger; source-backed facts require human review.]

## Skill Version(s):

0.1.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
