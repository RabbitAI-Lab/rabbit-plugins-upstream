## Description:

Guides Odia-speaking users through PowPow account registration, troubleshooting, and subscription activation without collecting credentials or performing payment actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Odia-speaking PowPow users use this skill to understand the product, open the correct registration and subscription pages, resolve common sign-up errors, and know what to do next. The agent provides guidance only; users complete forms, verification, and payment in the PowPow browser or app experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may disclose passwords, verification codes, or payment credentials while following registration and activation guidance.

Mitigation: Keep registration, verification, and payment actions in the PowPow browser or app flow; do not ask for passwords, verification codes, or payment credentials, and do not submit forms or payments for the user.

Risk: The skill describes a third-party service whose registration or subscription behavior may change after publication.

Mitigation: Use the live PowPow pages as the final authority for current fields, errors, and payment availability, and avoid inventing platform rules when the documented guidance does not match the current page.

Risk: Externally hosted screenshots or product links may be unavailable or stale.

Mitigation: Use the documented hosted screenshot links and jsDelivr fallback when needed, send only relevant screenshots, and continue with text guidance if images are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-or)
- [PowPow official website](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](artifact/references/registration-flow.md)
- [Payment and activation reference](artifact/references/payment-and-activation.md)
- [Product screenshots reference](artifact/references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain-text guidance with links, troubleshooting steps, and a clear next-step block]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; no scripts, local execution, registration automation, credential collection, or payment handling.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
