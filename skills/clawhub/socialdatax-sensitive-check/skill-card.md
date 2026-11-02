## Description:

用于敏感词检测、违禁词检测、文案发布前检查、内容安全检查、文案合规审核、能不能发判断、平台风险提示和改写建议。支持小红书、抖音、快手和通用文本场景，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者和运营人员可在发布前检查文案，获取敏感或违禁内容提示、风险等级及改写建议。支持通用文本，以及小红书、抖音和快手场景。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for checking and its structured results may be retained by SocialDataX.

Mitigation: Submit only text you are comfortable having the service retain; remove secrets and sensitive personal information before checking.

Risk: API use may incur charges.

Mitigation: Review the service's current pricing and monitor account usage before sending large volumes of text.

Risk: The documented command uses a package version that may change over time.

Mitigation: Review and pin a CLI version before use, and limit its access to unrelated files and credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-sensitive-check)
- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [JSON results summarized as concise text or Markdown]

**Output Parameters:** [1D (one text input, with an optional platform context)]

**Other Properties Related to Output:** [May include violation status, risk level, detected categories, highlighted excerpts, and rewrite suggestions. Text and structured results may be retained by SocialDataX.]

## Skill Version(s):

0.1.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
