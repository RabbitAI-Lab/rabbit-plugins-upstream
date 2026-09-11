## Description:

房地产风险分析专家 supports real-estate due diligence workflows for property data collection, sell-through analysis, monetizable value estimation, developer risk review, and credit-underwriting deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriskinhaha](https://clawhub.ai/user/chriskinhaha)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, developers, and due-diligence teams use this skill to collect and normalize real-estate project data, assess sell-through and cash-recovery posture, and prepare structured risk and credit-underwriting materials. It is oriented toward repeatable project, city, and developer analysis rather than one-off lookup only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes operational anti-bot, WAF, token-replay, and CDP bypass guidance that may be inappropriate outside authorized real-estate due-diligence work.

Mitigation: Install and use only for authorized due-diligence workflows; remove or tightly gate bypass playbooks and require explicit authorization and rate-limit controls before data collection.

Risk: Persistent agent-behavior updates may alter future automation prompts, memory, or skill behavior without sufficient review.

Mitigation: Require confirmation before writing memory, updating skills, or changing automation prompts, and review those changes before deployment.

Risk: Network collection guidance may require transport-security review before production use.

Mitigation: Re-enable TLS verification and review network settings before running collection workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chriskinhaha/skills/real-estate-risk-analyst)
- [CHANGELOG](artifact/CHANGELOG.md)
- [Real-estate collection technical guide](artifact/references/real-estate-guide.md)
- [33-city capability matrix](artifact/references/33城总表v6.md)
- [City onboarding checklist](artifact/references/城市接入checklist.md)
- [Due-diligence report template](artifact/references/尽调报告模板.md)
- [City run case library](artifact/references/城市实跑案例库.md)
- [Risk and anti-bot type catalog](artifact/references/类型库.md)
- [Ruishu/WAF handling notes](artifact/references/瑞数专项.md)
- [Shenzhen real-estate information platform](https://fdc.zjj.sz.gov.cn/szfdcscjy/projectPublish)
- [Hefei real-estate market information platform](https://www.hfzfzlw.com/spf)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional Python, batch, JSON, Excel, and HTML artifact instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or generate scripts, dashboards, spreadsheets, and due-diligence report structures depending on the agent task.]

## Skill Version(s):

2.0.0 (source: release evidence and CHANGELOG, released 2026-09-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
