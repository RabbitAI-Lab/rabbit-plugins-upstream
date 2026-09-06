## Description:

Buffer API integration with managed authentication for scheduling and managing social media posts across multiple platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Buffer through Maton, inspect Buffer account and channel data, and create or schedule social media posts with explicit confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can schedule or publish social media content through the connected Buffer account.

Mitigation: Default to read and list operations, then require explicit user confirmation of the target channel, payload, and intended effect before any write.

Risk: A raw Maton API key fallback can expose a long-lived credential if printed, logged, or persisted.

Mitigation: Prefer OAuth through the Maton CLI; use the raw API key only where the CLI cannot be installed, and never print, log, or store the key.

Risk: Ambiguous Buffer connections or Maton profiles can send requests to the wrong account or channel.

Mitigation: Confirm the exact connection and target channel, and specify the connection or profile when more than one is available.

Risk: Deleting a Buffer connection revokes stored authorization and can break automation using that connection.

Mitigation: List connections, match the specific connection ID with the user, and get confirmation before deletion.

Risk: Buffer responses can include personal data and unpublished content.

Mitigation: Request and show only the fields needed for the task, and avoid dumping full responses into logs or files.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Buffer API Documentation](https://developers.buffer.com/reference.html)
- [Buffer API Getting Started](https://developers.buffer.com/guides/getting-started.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell, GraphQL, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include account, channel, post, and scheduling data; responses should be minimized to the fields needed for the user's task.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
