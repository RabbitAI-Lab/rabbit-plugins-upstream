## Description: <br>
Parses WeChat group Jielong order text into product lists, participant order details, pivot tables, totals, and optional Tencent Docs exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dingguotu](https://clawhub.ai/user/dingguotu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to turn pasted WeChat group-buying Jielong messages into structured per-participant order tables, product summaries, totals, and shareable Tencent Docs spreadsheets when the connector is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Parsed WeChat order data can include nicknames, room numbers, purchases, and totals that are exported to Tencent Docs when the connector is available. <br>
Mitigation: Use the skill only when participants expect an online spreadsheet, and review the Tencent Docs access settings before sharing the link. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dingguotu/skills/wechat-jielong-parser) <br>
- [Publisher profile](https://clawhub.ai/user/dingguotu) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration] <br>
**Output Format:** [Markdown tables and optional Tencent Docs spreadsheet links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include parsed product columns, participant rows, order totals, ambiguity notes, and Tencent Docs export links when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
