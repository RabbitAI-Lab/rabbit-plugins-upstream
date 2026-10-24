## Description:

用 Cue 穿透人物的全生命周期工商与司法轨迹——剥离当前在册与历史风险、映射其商业控制版图，产出可用于 IPO 或重大交易的个人背调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向 IPO、重大交易、合作方准入及高管候选人核查等场景，整理人物的公开工商、司法与行政处罚信息及其商业关联。用于雇佣或信贷等决策前，应遵守适用法律并取得必要同意；正式使用前由专业人士核验底稿。

### Deployment Geography for Use:

China; comply with applicable local laws and privacy requirements.

## Known Risks and Mitigations:

Risk: The downloaded runner recommends disabling agent restrictions if connections fail.

Mitigation: Keep agent restrictions enabled and review a fixed runner revision before execution.

Risk: A Cue API key may be exposed if shared in chat.

Mitigation: Configure the key locally and do not send it through chat.

Risk: Research runs can consume account credits.

Mitigation: Check expected usage and available credits before starting a run.

Risk: Background-check reports may be incomplete or incorrect and can affect sensitive decisions.

Mitigation: Verify findings against linked public records, obtain required consent, and have a qualified professional review the report before formal use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-person-background-check)
- [Cue](https://cuecue.cn/)
- [National Enterprise Credit Information Publicity System](https://www.gsxt.gov.cn)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [China Enforcement Information Disclosure](https://zxgk.court.gov.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Structured Chinese Markdown due-diligence report with linked public sources and business-relationship findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research notes only; source records and conclusions require professional verification before formal use.]

## Skill Version(s):

1.0.8 (source: server-resolved release evidence; artifact frontmatter states 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
