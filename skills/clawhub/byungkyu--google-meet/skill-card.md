## Description:

Google Meet API integration with managed OAuth for creating meeting spaces, listing conference records, and managing meeting participants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Google Meet through Maton OAuth, read meeting records, manage spaces and participants, and set up user-approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Google Meet data available to the connected account, including meeting records, participants, recordings, and transcripts.

Mitigation: Use OAuth where possible, choose only the scopes needed for the task, and avoid raw API keys unless the CLI cannot be used.

Risk: Write operations or automations can change Google Meet resources or move meeting data through trigger destinations.

Mitigation: Confirm every write or automation setup with the user and keep trigger destinations narrowly scoped.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-meet)
- [Maton homepage](https://maton.ai)
- [Google Meet API Overview](https://developers.google.com/meet/api/reference/rest)
- [Google Meet Spaces](https://developers.google.com/meet/api/reference/rest/v2/spaces)
- [Google Meet Conference Records](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords)
- [Google Meet Participants](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.participants)
- [Google Meet Recordings](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.recordings)
- [Google Meet Transcripts](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.transcripts)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger catalog](references/calendly/triggers.md)
- [GitHub trigger catalog](references/github/triggers.md)
- [Google Mail trigger catalog](references/google-mail/triggers.md)
- [HubSpot trigger catalog](references/hubspot/triggers.md)
- [Linear trigger catalog](references/linear/triggers.md)
- [Notion trigger catalog](references/notion/triggers.md)
- [Slack trigger catalog](references/slack/triggers.md)
- [Stripe trigger catalog](references/stripe/triggers.md)
- [Time trigger catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for authenticated Google Meet operations through Maton; responses may include sensitive meeting data from the connected account.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
