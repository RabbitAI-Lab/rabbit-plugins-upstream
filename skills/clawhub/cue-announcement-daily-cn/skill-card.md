## Description:

按公司或自选清单整理指定日期窗内的 A 股公告，逐条列出披露日期、公告标题、关键数字和来源，并将投资判断留给人工。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

面向关注 A 股公告的用户，按公司或用户提供的自选清单汇总指定日期窗内的披露事项，并保留标题、日期、关键数字和来源定位，供用户核对原文。评级、目标价和走势判断由人工处理。

### Deployment Geography for Use:

Global; covers companies listed in mainland China's A-share market.

## Known Risks and Mitigations:

Risk: Queries can reveal which companies interest the user.

Mitigation: Use user-supplied filings when that privacy concern matters.

Risk: An API key could be exposed or sent to an unintended destination.

Mitigation: Keep the key out of chat and verify the provider destination uses HTTPS before authenticating.

Risk: Optional installers and skills are outside this package review.

Mitigation: Review and pin optional installers and skills separately.

## Reference(s):

- [Cue data connection guide](https://cuecue.cn/hub/mcp)
- [Cue attachment reader guide](https://cuecue.cn/hub/omni-reader)
- [Cue API key guide](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Four-section Markdown announcement digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each filing entry includes its disclosure date, verbatim title, key figures, and source anchor. Missing information is called out; ratings, price targets, and market direction are marked for human review.]

## Skill Version(s):

0.1.1 (source: CHANGELOG, released 2026-11-02)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
