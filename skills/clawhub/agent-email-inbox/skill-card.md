## Description:

Gives an AI agent its own real email inbox for sending mail, receiving replies, threading conversations back to the agent, and acting on inbound email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diyanbogdanov](https://clawhub.ai/user/diyanbogdanov)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill to provision an Anima inbox for an agent, send and read email, preserve reply threading, and receive inbound-mail webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to globally install and run an unpinned third-party CLI that can change over time.

Mitigation: Review the Anima CLI package before use and prefer a pinned version installed in an isolated environment.

Risk: Outbound email capability can affect external recipients if enabled for an untrusted or poorly controlled agent.

Mitigation: Only enable send capability for trusted agents, keep owner verification in the loop, and use the test-send mode for rehearsals or CI.

Risk: Message contents, recipients, inbound mail, API keys, and webhook payloads may contain sensitive data.

Mitigation: Handle email data and API keys as sensitive, and verify webhook signatures before trusting inbound payloads.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/diyanbogdanov/skills/agent-email-inbox)
- [Anima Homepage](https://useanima.sh)
- [Anima Documentation](https://docs.useanima.sh)
- [Anima API Base](https://api.useanima.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline bash and curl code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes CLI commands for inbox provisioning, email send/read/search, owner verification, test sends, threaded replies, and inbound webhook setup.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
