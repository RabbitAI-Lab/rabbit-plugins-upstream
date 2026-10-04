## Description:

Guides developers integrating WeChat payments and Official Account OAuth with CloudBase, including generated functions, callbacks, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building CloudBase applications use this skill to add or troubleshoot Mini Program and Official Account payment, virtual payment, QR-code checkout, OAuth, and payment callbacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated payment or callback code could mishandle orders or fulfillment.

Mitigation: Review generated code and confirm payment with server-side callbacks or order queries before fulfillment.

Risk: Merchant keys and Official Account credentials could be exposed in chat or source code.

Mitigation: Configure secrets in the CloudBase or WeChat console; do not paste them into chat or embed them in code.

Risk: Real payments or deployment could change live systems.

Mitigation: Require explicit user approval before real-payment tests or deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [Mini Program WeChat Pay guide](references/mini-program-pay.md)
- [Mini Program virtual payment guide](references/virtual-payment.md)
- [Official Account OAuth guide](references/official-account-oauth.md)
- [WeChat integration troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance; generated payment and callback code requires review.]

## Skill Version(s):

1.2.55 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
