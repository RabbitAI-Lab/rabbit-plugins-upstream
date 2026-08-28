## Description:

Query and act on Evite events, guest lists, RSVPs, and messages from a shell with curl and a cookie jar, using Evite internal /services/, /ajax/, and /tsunami/ endpoints instead of running the evite-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Evite event data and prepare shell commands for authorized RSVP, guest-list, message, photo, and event-management workflows without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read private Evite event and guest data.

Mitigation: Use only Evite accounts and events the operator is authorized to access, keep cookie jars private, and avoid sharing logs that contain guest data or cookies.

Risk: The skill can perform account-changing actions such as RSVPs, guest edits, broadcasts, sends, uploads, cancellations, and reinstatements.

Mitigation: Manually confirm every write action before running the command, and test sends or broadcasts only against a throwaway event.

Risk: Some write request bodies are documented as assumed rather than fully verified.

Mitigation: Treat assumed request bodies as lower confidence, verify the target event state after use, and avoid blind retries after ambiguous responses.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local cookie jar and fresh CSRF token handling for authenticated reads and writes.]

## Skill Version(s):

0.6.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
