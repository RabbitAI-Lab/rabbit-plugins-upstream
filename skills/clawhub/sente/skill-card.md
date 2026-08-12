## Description:

Sente gives an agent a durable email identity and account automation workflows for sending and receiving mail, waiting for verification codes or magic links, registering accounts, and connecting user-owned accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shim2k](https://clawhub.ai/user/shim2k)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent needs its own email inbox, must retrieve verification codes or magic links, or needs authorized account signup, login, and relogin workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages durable email identities, inbox access, account signup, login, credentials, exported sessions, API tokens, and related account automation.

Mitigation: Install only when the agent should perform those actions, store tokens and exported sessions as sensitive secrets, avoid printing or committing credentials, and revoke or delete connections when access is no longer needed.

Risk: Autonomous account registration or login can be inappropriate for sites where automation is restricted or where user review is required.

Mitigation: Use confirm-before-submit for sensitive or unclear targets, register only accounts the user's organization is accountable for, and hand blocked steps such as CAPTCHA or MFA to a human.

Risk: Inbound email can contain untrusted content that attempts to influence the agent.

Mitigation: Use extracted verification artifacts such as OTP codes or magic links only, and do not treat email body instructions as user or system instructions.

## Reference(s):

- [Sente service integration guide](https://sente.run/skill.md)
- [Sente service site](https://sente.run)
- [ClawHub Sente skill page](https://clawhub.ai/shim2k/skills/sente)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce sensitive CLI outputs such as API-token handling instructions, OTPs, magic links, account identifiers, credential metadata, webhook details, and browser session export paths.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
