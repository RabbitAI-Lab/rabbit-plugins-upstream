## Description:

Agent Email Inbox gives an AI agent its own real email address for sending, receiving, threading replies, and acting on inbound email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill when an agent needs a dedicated inbox, outbound email authority, threaded replies, email search, or inbound email webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global CLI installation can weaken supply-chain controls in stricter environments.

Mitigation: Use a project-local or pinned Anima CLI version before installing or running commands.

Risk: Outbound email capability lets trusted agents communicate externally.

Mitigation: Enable sending only for agents trusted to communicate externally and complete owner verification before full send capability is used.

Risk: The ANIMA_API_KEY grants access to the Anima API.

Mitigation: Protect ANIMA_API_KEY as a secret and avoid exposing it in logs, prompts, or shared files.

Risk: Inbound webhook payloads could be acted on before authenticity is established.

Mitigation: Verify webhook signatures before trusting or processing inbound email events.

## Reference(s):

- [Anima Homepage](https://useanima.sh)
- [Anima Documentation](https://docs.useanima.sh)
- [Anima API Base](https://api.useanima.sh)
- [ClawHub Skill Page](https://clawhub.ai/anima/skills/agent-email-inbox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands, API request examples, and webhook verification guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
