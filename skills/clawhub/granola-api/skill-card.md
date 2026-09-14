## Description:

Granola lets an agent search, summarize, list, and retrieve the user's Granola meeting notes and transcripts through Maton-managed MCP authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to answer questions about meeting content, find action items, retrieve meeting details, and review transcripts from an authorized Granola account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the Maton CLI from an untrusted source or with unnecessary administrator privileges could expose the local environment.

Mitigation: Use trusted Maton package sources, keep installs unprivileged where possible, and review release notes before changing pinned versions.

Risk: API keys and OAuth credentials can expose Granola meeting data if copied into files, logs, command lines, or trigger destinations.

Mitigation: Prefer OAuth, let the CLI and operating-system credential store handle tokens, and never embed Maton or provider credentials in scripts, logs, environment dumps, or destination payloads.

Risk: Granola responses may contain sensitive meeting notes, transcripts, decisions, participant identities, and customer or personnel information.

Mitigation: Request only the meetings and fields needed for the task, return the narrowest useful answer, preserve source citations, and get explicit informed approval before forwarding meeting content or enabling automation.

Risk: Trigger destinations can create persistent forwarding of future event data.

Mitigation: Create or update destinations only after a separate user approval that names the destination, data flow, and automation scope.

## Reference(s):

- [Granola Skill Page](https://clawhub.ai/byungkyu/skills/granola-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Granola MCP Documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp)
- [Granola Help Center](https://docs.granola.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Query Granola Meetings Schema](schemas/query_granola_meetings.json)
- [List Meetings Schema](schemas/list_meetings.json)
- [Get Meetings Schema](schemas/get_meetings.json)
- [Get Meeting Transcript Schema](schemas/get_meeting_transcript.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and schema-backed API call patterns.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent outputs may include Granola meeting-note answers, citations, meeting metadata, transcript excerpts, and approval prompts for connection, write, or automation actions.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
