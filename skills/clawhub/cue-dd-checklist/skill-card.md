## Description:

为单一 A 股公司整理带披露来源锚点的公开信息风险事实表和九类覆盖率对账表，不提供投资或法律意见。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向投资、授信和并购团队，对单一 A 股公司做投前初筛、背景核查或并购线索整理。输出逐条带披露锚点的风险事实，以及说明已查、零结果和无可用工具类别的覆盖率账。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection setup may expose the optional API key.

Mitigation: Start with user-supplied disclosures and no API key; before enabling credentials, verify destination checks for the documented requests and redirects.

Risk: Automated checks may miss a company attribution mismatch.

Mitigation: Compare company names and identifiers against the original disclosures even when validation passes.

Risk: The optional document reader's handling of confidential files is uncertain.

Mitigation: Confirm where the reader sends documents before providing confidential material, and review installer and dependency revisions.

## Reference(s):

- [Channel map](artifact/references/channel-map.md)
- [Coverage map template](artifact/references/coverage-map-template.md)
- [Cue data MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Markdown, JSON Lines, Guidance]

**Output Format:** [Markdown risk fact table and coverage ledger, with a JSON Lines source index and run log]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-company, date-bounded research; each listed fact is expected to resolve to a disclosure source.]

## Skill Version(s):

0.1.34 (source: SKILL.md frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
