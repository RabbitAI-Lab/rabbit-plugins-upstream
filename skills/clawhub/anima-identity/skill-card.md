## Description:

Gives an AI agent a real email inbox, US phone number for SMS and voice, and encrypted credential vault through Anima.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diyanbogdanov](https://clawhub.ai/user/diyanbogdanov)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to provision and operate an agent-owned email inbox, phone/SMS identity, voice calling path, and credential vault with human verification and plan controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to use real external communications channels and credential-handling capabilities.

Mitigation: Use it only when an agent is intended to operate its own email or phone identity, and require clear human approval for account signups, OTP/2FA handling, SMS/calls, and organization-wide webhooks.

Risk: Exposed Anima API keys could allow impersonation of the agent identity.

Mitigation: Keep Anima API keys out of model-visible memory and chat history; use a secret manager or protected environment variable, rotate exposed keys, and send keys only to api.useanima.sh.

Risk: Phone and voice use can create consent, verification, or compliance obligations.

Mitigation: Call or text only numbers where the user has the required consent, and have a human confirm calling restrictions, verification flows, and plan-gated capabilities before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/diyanbogdanov/skills/anima-identity)
- [Anima homepage](https://useanima.sh)
- [Anima documentation](https://docs.useanima.sh)
- [Anima agent documentation feed](https://docs.useanima.sh/llms.txt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request examples, setup steps, plan or verification status guidance, and security handling guidance.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
