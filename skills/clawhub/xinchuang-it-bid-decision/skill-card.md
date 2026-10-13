## Description:

基于历史招投标数据评估IT项目的投标价值、竞争格局、报价参考和潜在风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

投标团队可输入具体IT招标项目，获取采购方历史、潜在竞争者、报价区间及投标风险分析，辅助决定是否参与。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account registration can fingerprint a device and create locally stored API credentials.

Mitigation: Provide your own ZLBX_API_KEY to skip registration; require informed consent before registering and remove stored credentials when no longer needed.

Risk: Generated reports and signed source links may disclose share-sensitive project information or grant access to linked records.

Mitigation: Review reports and signed links before sharing, and limit access to their saved copies.

Risk: Historical procurement data and inferred competitor or price estimates can be incomplete or misleading for business decisions.

Mitigation: Check cited records, data gaps and current tender requirements independently before making a bid decision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/xinchuang-it-bid-decision)
- [Analysis workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, HTML reports]

**Output Format:** [Markdown decision report and optional shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a recommendation, supporting evidence, pricing range, risk assessment and source links; full analyses normally export an HTML copy.]

## Skill Version(s):

1.0.6 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
