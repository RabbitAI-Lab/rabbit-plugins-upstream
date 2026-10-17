## Description:

Helps agents read a signed-in user's MyAtriumHealth records, including test results, medications, allergies, immunizations, health issues, visits, goals, and messages, through a Chrome browser session and shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Patients and their authorized assistants use this skill to retrieve and filter their own MyAtriumHealth records from a signed-in browser session for scripts or one-off queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension and fpx profile can access a signed-in health portal session, and pairing persists.

Mitigation: Review the third-party CLI and extension before use; remove or revoke the fpx profile when persistent pairing is no longer needed.

Risk: Command output can expose sensitive personal health information in logs or chats.

Mitigation: Filter responses to only necessary fields and avoid pasting full responses into logs or chats.

Risk: Expired sessions or an unavailable browser tab can produce empty or misleading responses.

Mitigation: Check the signed-in session and open tab before relying on empty results; sign in again when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [Endpoint recipes](references/endpoints.md)
- [Shell helpers](references/mah.sh)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results can contain sensitive personal health information; filter results before sharing.]

## Skill Version(s):

1.3.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
