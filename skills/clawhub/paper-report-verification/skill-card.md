## Description:

为用户核对维普、万方和中国知网的论文查重、AIGC、格式与智评报告提供官方验真入口、字段填写、复制方法、图文步骤和结果核对指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zslzxy](https://clawhub.ai/user/zslzxy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to identify a paper report brand, open the correct official verification entry, locate required report fields, and compare returned records without sharing full reports or credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may submit report details to unofficial or spoofed verification pages.

Mitigation: Confirm the destination is the correct official page for the report brand before entering report details, and do not treat links inside a report or screenshot as trusted.

Risk: Users may expose sensitive academic or personal report data while seeking verification help.

Mitigation: Do not provide account passwords, full reports, CAPTCHA values, real report numbers, names, titles, order numbers, or report body text to the agent.

Risk: A successful verification result may be mistaken for proof that the paper meets academic requirements.

Mitigation: Treat verification as evidence of a matching official record only; separately evaluate academic compliance, similarity, AIGC, formatting, or review outcomes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zslzxy/skills/paper-report-verification)
- [Report verification tutorial](artifact/references/tutorial.md)
- [Report verification page notes](artifact/references/browser-pages.md)
- [Report verification lane contract](artifact/references/contract.md)
- [Unified official verification entry](https://vpcs.cqccjy.cn/pwp/verify)
- [Wanfang verification page](https://truth.wanfangdata.com.cn/)
- [CNKI verification page](https://check7.cnki.net/codeverify/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Chinese Markdown with step-by-step instructions, tables, official links, and image references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses placeholders or redacted examples and avoids collecting passwords, CAPTCHA values, full reports, or unredacted report data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
