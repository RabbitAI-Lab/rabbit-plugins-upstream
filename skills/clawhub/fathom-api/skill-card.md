## Description:

Fathom API integration with managed OAuth for retrieving meeting recordings, transcripts, summaries, action items, teams, team members, and managing webhooks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Fathom meeting data, search recordings, retrieve transcripts and summaries, and configure webhook notifications through a Maton-managed connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive meeting recordings, transcripts, summaries, action items, and webhook payloads.

Mitigation: Prefer OAuth, request only the scopes needed for the task, avoid printing or storing credentials, and extract only the fields the user needs from responses.

Risk: Calls with destination_url can send transcript or summary content to an external host even when the API method is GET.

Mitigation: Treat destination_url as an egress action requiring explicit user confirmation of the host, controller, and content before making the call.

Risk: Webhooks can create a standing pipeline that pushes future meeting content automatically.

Mitigation: Confirm webhook destination, payload flags, triggered_for scope, and ongoing delivery with the user; scope triggered_for narrowly and leave transcripts off unless required.

Risk: The Maton API passthrough can reach endpoints beyond the documented examples when the connection permits it.

Mitigation: Default to read and list calls, verify account and resource identifiers first, and require explicit user approval before writes, deletes, new connections, or other side-effecting operations.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Fathom API Documentation](https://developers.fathom.ai)
- [Fathom LLM Reference](https://developers.fathom.ai/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/fathom-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe OAuth setup, Maton CLI commands, raw HTTP fallback, Fathom API paths, and safety confirmations for writes and egress actions.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
