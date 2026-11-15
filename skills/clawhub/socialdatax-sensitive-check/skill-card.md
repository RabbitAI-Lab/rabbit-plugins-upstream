## Description:

用于敏感词检测、违禁词检测、文案发布前检查、内容安全检查、文案合规审核、能不能发判断、平台风险提示和改写建议。支持小红书、抖音、快手和通用文本场景，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要发布社交媒体文案的内容创作者与运营人员，检查文本在小红书、抖音、快手或通用场景中的敏感词和风险，并获取风险提示与改写建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags an unpinned CLI package, creating supply-chain risk around credentials and other available data.

Mitigation: Review the package source and use a trusted, pinned release; enter API credentials only through the documented local authentication flow.

Risk: The security scan is incomplete because some local references could not be resolved.

Mitigation: Review the complete package and the unresolved references before use.

Risk: The service stores submitted text and structured results for history, billing, and troubleshooting.

Mitigation: Submit only text approved for processing by the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-sensitive-check)
- [SocialDataX skill and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Concise text or Markdown with risk findings and rewrite suggestions; the CLI response is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checks text for a selected platform context and provides findings and suggestions when available. The documented v1 supports text only.]

## Skill Version(s):

0.1.14 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
