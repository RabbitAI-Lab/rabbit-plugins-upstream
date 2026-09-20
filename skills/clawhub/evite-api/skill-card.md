## Description:

Query and act on Evite events, guest lists, RSVPs, and messages from a shell with curl and a cookie jar instead of running the evite-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Evite event data and prepare shell commands for authenticated Evite read and write operations, including guest lists, RSVP summaries, messages, invitations, photos, and event lifecycle actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Evite credentials and a live session cookie jar.

Mitigation: Use restricted cookie-jar permissions, avoid sharing session files, and prefer low-impact or throwaway Evite events for first use.

Risk: Generated commands can mutate live Evite data, email guests, delete guests, send invitations, upload photos, or cancel events.

Mitigation: Manually verify event IDs, guest IDs, recipient counts, and message bodies, and require explicit confirmation before executing any write action.

Risk: Some write bodies are documented as assumed rather than fully verified.

Mitigation: Treat assumed request bodies as higher risk, test them against a throwaway event, and re-check Evite responses before repeating the operation.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)
- [Evite](https://www.evite.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an authenticated cookie jar and fresh CSRF token guidance for live Evite operations.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
