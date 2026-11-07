## Description:

用 Cue 通常 5-10 分钟（最长约 15 分钟）实时扫描今日 A 股热点板块与近 24h 催化资讯，拆解盘中催化逻辑与受益方向；跑完自动生成「看板图」与「报告长图」，报告全文以 Cue 链接交付。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to review intraday A-share sector activity, related news catalysts, potential beneficiary directions, and market risks. It produces a concise dashboard and a longer report for further review.

### Deployment Geography for Use:

China (A-share market)

## Known Risks and Mitigations:

Risk: The setup guidance asks users to send an API key through chat.

Mitigation: Configure the key locally instead of sharing it in chat, and rotate any key already shared.

Risk: The external runner is outside the inspected skill bundle.

Mitigation: Review and pin the runner before executing it.

Risk: Untrusted JSON can affect dashboard tone values during rendering.

Mitigation: Strictly validate tone values before rendering dashboard data.

Risk: Scheduled reports consume credits and continue until disabled.

Mitigation: Enable scheduled runs only when intended, monitor their credit use, and disable them when no longer needed.

## Reference(s):

- [Cue intraday report service](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-hotspot-tracker)
- [SOP dashboard schema](artifact/references/sop-schema.md)
- [Eastmoney market information source](https://www.eastmoney.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Image files, Links]

**Output Format:** [Markdown report, structured dashboard JSON, and dashboard/report images (PNG when browser support is available; otherwise HTML)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize intraday A-share market activity and may include a Cue share link; scheduled runs consume Cue credits.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
