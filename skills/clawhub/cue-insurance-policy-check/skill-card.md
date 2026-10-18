## Description:

用 Cue 核验保险产品的保障责任、免责、等待期、费率与退保损失，对比同类产品并生成供客户如实说明的条款理解底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

保险从业者和产品团队可核对产品保障、免责及退保条款，比较同类产品，并准备向客户如实说明的底稿。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs externally maintained code while using a local Cue API key.

Mitigation: Install only if you trust the runner and Cue service; review runner changes before execution and use a Cue-specific, least-privilege key.

Risk: Insufficient credits can lead to referral or payment prompts.

Mitigation: Treat referrals and payments as optional; explain available alternatives without pressuring users.

Risk: Insurance comparisons can depend on incomplete or outdated external sources.

Mitigation: Check material findings against current insurer policy documents before using them with customers.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-insurance-policy-check)
- [Cue runner referenced by the skill](https://github.com/sensedeal/cue-skills)
- [Cue platform](https://cuecue.cn/)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown report with source links and a Cue report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report covers coverage, exclusions, premiums, surrender losses, comparisons, and claims that should not be promised.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
