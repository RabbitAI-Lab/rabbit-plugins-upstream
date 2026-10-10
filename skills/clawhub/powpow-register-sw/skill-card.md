## Description:

Guides Swahili-speaking users through PowPow account registration, Alipay subscription activation, and sign-in, with an assisted or manual path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Swahili-speaking users can ask an agent to create and activate a PowPow account, complete email verification, open an Alipay payment page, and receive a sign-in link. If automated assistance is unavailable, the skill gives manual registration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Assisted registration handles real account credentials and email verification codes.

Mitigation: Use only for an account you intend to create; keep passwords and verification codes private and avoid sharing transcripts containing them.

Risk: The agent can create a payment order and open an Alipay checkout page.

Mitigation: Confirm the subscription and price before order creation; complete payment yourself at checkout.

Risk: Generated one-click sign-in links grant account access if shared.

Mitigation: Treat sign-in links as sensitive, avoid sharing screenshots or transcripts containing them, and run cleanup when finished.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-sw)
- [Agent workflow](artifact/references/agent-flow.md)
- [Registration guidance](artifact/references/registration-flow.md)
- [Payment and activation guidance](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Conversational text with commands and registration, payment, and sign-in links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can share bundled product screenshots; sign-in links are sensitive.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
