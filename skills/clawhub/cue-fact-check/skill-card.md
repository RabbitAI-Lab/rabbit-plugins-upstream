## Description:

用 Cue 穿透待核查资讯的表层表述——通过独立信源交叉验证与底层数据复核，精准识别时间错位、数据偏差及误导性信息，产出包含原文对照与纠偏证据的结构化事实核查报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

外部用户可将研报、新闻、尽调材料或市场传言交由该 Agent 核验；它会对关键主张进行多源交叉验证，并整理原文、结论、纠偏证据和来源链接。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fact-checking workflow sends claims to Cue, so private material may be disclosed to the service.

Mitigation: Submit only material that is appropriate to share with Cue; keep API keys in local configuration rather than chat.

Risk: The downloaded runner can change, and its code and server-side processing are not verified by the bundled artifact.

Mitigation: Review and pin the external runner before installation, and rotate any API key already shared.

Risk: The workflow contains mandatory promotional prompts that could pressure users toward paid or referral actions.

Mitigation: Remove mandatory promotion and preserve the user's ability to cancel or decline.

## Reference(s):

- [Cue 平台](https://cuecue.cn)
- [Cue API Key 管理](https://cuecue.cn/api-key?src=clawhub-fact-check)
- [事实核查报告示例](https://cuecue.cn/share/680abf29664d)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Structured Markdown fact-check report with claim-by-claim findings, evidence comparisons, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the checked source text alongside conclusions and corrective evidence.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
