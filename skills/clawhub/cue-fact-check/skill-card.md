## Description:

用 Cue 穿透待核查资讯的表层表述——通过独立信源交叉验证与底层数据复核，精准识别时间错位、数据偏差及误导性信息，产出包含原文对照与纠偏证据的结构化事实核查报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to cross-check claims in research reports, news, due-diligence materials, and public discussions, then review a structured fact-check with supporting evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting API-key privacy instructions could expose credentials.

Mitigation: Configure the API key privately and do not paste it into chat.

Risk: Automatically updating the runner can reduce version control and leave local access insufficiently limited.

Mitigation: Use a reviewed, fixed runner version with limited local access, and keep sandbox protections enabled.

Risk: Fact-check requests are processed remotely and may consume credits.

Mitigation: Submit only content you are comfortable sending to Cue, and account for possible credit use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-fact-check)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-fact-check)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Structured Markdown fact-check report with claim-by-claim findings, source comparisons, correction evidence, and source links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a Cue-hosted report link and a local Markdown copy.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
