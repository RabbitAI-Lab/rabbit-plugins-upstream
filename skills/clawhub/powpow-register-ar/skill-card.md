## Description:

يساعد المستخدمين بالعربية على فهم PowPow (بابل)، إنشاء حساب، تشخيص مشكلات التسجيل، وتفعيل الاشتراك بعد الدفع.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Arabic-speaking PowPow users use this skill to move from product introduction through account registration, verification troubleshooting, and subscription activation. The skill provides step-by-step guidance while the user completes account creation, credentials, verification codes, and payment directly in PowPow pages or apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose passwords, verification codes, or payment details during assisted registration.

Mitigation: The skill instructs the assistant not to request credentials, verification codes, or payment data; users complete those steps directly in PowPow pages or apps.

Risk: Payment and account activation could be misunderstood as actions the assistant performs.

Mitigation: The skill frames payments and activation as user-controlled browser or app actions and limits assistant output to navigation and troubleshooting guidance.

Risk: Public screenshot links or PowPow pages may fail to load for some users.

Mitigation: The skill includes fallback screenshot hosting guidance and direct PowPow registration and subscription URLs.

## Reference(s):

- [PowPow official site](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [تفاصيل عملية التسجيل](references/registration-flow.md)
- [تفعيل الاشتراك والدفع](references/payment-and-activation.md)
- [لقطات شاشة واجهة المنتج](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions]

**Output Format:** [Arabic Markdown guidance with links and step-by-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance-only output; no code execution, credential collection, or payment processing.]

## Skill Version(s):

1.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
