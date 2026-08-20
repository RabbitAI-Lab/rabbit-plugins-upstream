## Description:

Use when researching China market, industry, macro, trade, procurement, listed-company disclosure, regulation, IP, healthcare, logistics, energy, environment, or industrial-operation information using free official sources with no registration, no API key, and no cryptocurrency data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, developers, and business researchers use this skill to gather China market, regulatory, procurement, and listed-company disclosure evidence from official free public sources. It also helps agents query CNINFO A-share announcements through the included no-key helper and cite source URLs, metric definitions, and time ranges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may browse official Chinese market and regulatory sites and run the CNINFO query helper.

Mitigation: Use it only when this browsing and helper execution are acceptable for the task, and review cited URLs, metric definitions, and time ranges before relying on conclusions.

Risk: Supplying login cookies, API keys, or personal sensitive data could expose information to external sites or logs.

Mitigation: Do not provide credentials or personal sensitive data unless there is a separate approved reason and clear control over what will be sent.

Risk: Some sources may present login walls, CAPTCHA, signature requirements, or access protection.

Mitigation: Abandon those sources and use other official public sources; do not bypass access controls or request unauthorized interfaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-market-cn)
- [CNINFO](https://www.cninfo.com.cn/new/index)
- [National Bureau of Statistics data](https://data.stats.gov.cn/)
- [People's Bank of China statistics](https://www.pbc.gov.cn/diaochatongjisi/116219/index.html)
- [State Administration of Foreign Exchange statistics](https://www.safe.gov.cn/safe/tjsj1/index.html)
- [MOFCOM data center](https://data.mofcom.gov.cn/index.shtml)
- [China Government Procurement Network](https://www.ccgp.gov.cn/xxgg/)
- [National Public Resource Trading Platform](https://www.ggzy.gov.cn/)
- [China Securities Regulatory Commission](https://www.csrc.gov.cn/)
- [China National Intellectual Property Administration](https://www.cnipa.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON from the CNINFO helper.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should retain source URLs, metric definitions, and time ranges; the helper emits JSON for CNINFO announcement searches.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
