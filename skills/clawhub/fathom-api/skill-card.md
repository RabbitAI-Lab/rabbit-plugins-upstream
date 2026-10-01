## Description:

Connects an agent to Fathom through Maton to retrieve meeting recordings, transcripts, and summaries and manage approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Fathom can ask an agent to find meeting content and retrieve summaries or transcripts. With their approval, they can also configure webhooks or scheduled workflows through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting transcripts and summaries can disclose sensitive conversations to unintended recipients.

Mitigation: Limit retrieved content to what the task needs and confirm the exact destination and data shared before forwarding it.

Risk: Webhooks, callbacks, functions, and triggers can continue forwarding meeting data after setup.

Mitigation: Obtain explicit approval for the destination, payload, scope, and ongoing delivery; disable unused automations.

## Reference(s):

- [ClawHub Fathom skill](https://clawhub.ai/byungkyu/skills/fathom-api)
- [Maton](https://maton.ai)
- [Fathom API documentation](https://developers.fathom.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Scheduled trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands, code examples, and meeting-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may contain sensitive meeting information; automations require user approval.]

## Skill Version(s):

1.2.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
