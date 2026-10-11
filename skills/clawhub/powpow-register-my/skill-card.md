## Description:

Guides users through PowPow account registration, email verification, subscription activation, and sign-in during a conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide account signup, handle email verification and common registration issues, and prepare subscription activation while completing payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signup involves an email verification code and a password.

Mitigation: Share the code only for PowPow verification; avoid putting passwords in command arguments or saved files, and securely save any generated password.

Risk: The agent can create a payment order and monitor payment status.

Mitigation: Complete payment yourself through the official checkout; do not share payment credentials with the agent.

Risk: Registration may leave local session state after the flow.

Mitigation: Run the skill's cleanup step when finished to remove local session state.

## Reference(s):

- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-my)
- [PowPow homepage](https://global.powpow.online)
- [Agent-assisted registration flow](references/agent-flow.md)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Conversational text and Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide official checkout and sign-in links and report registration or payment status.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
