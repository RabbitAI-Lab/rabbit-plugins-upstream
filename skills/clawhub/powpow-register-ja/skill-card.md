## Description:

Guides Japanese-speaking users through PowPow account registration, troubleshooting, and subscription activation without handling credentials or payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support agents use this skill to introduce PowPow, walk through account registration, diagnose common registration issues, and guide users to the appropriate subscription activation path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share passwords, verification codes, or payment details in chat while following registration and subscription guidance.

Mitigation: The skill instructs the agent not to request credentials, verification codes, or payment information, and to keep registration and payment actions on PowPow pages.

Risk: Payment activation can be delayed or require manual confirmation depending on the channel.

Mitigation: The skill explains that PayPal activation may wait for webhooks, WeChat scan payments require manual confirmation, and Huawei IAP should be checked in app before escalating.

Risk: Screenshot links could be over-shared or mismatched to the user's current task.

Mitigation: The skill limits screenshots to one to three topic-relevant hosted images selected from its screenshots reference.

## Reference(s):

- [PowPow homepage](https://global.powpow.online)
- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-ja)
- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Screenshots reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown guidance with links and short next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guide-only responses; no code execution, form submission, credential handling, or payment processing.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
