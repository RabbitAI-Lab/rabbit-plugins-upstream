## Description:

Query and act on Evite events, guest lists, RSVPs, messages, invitations, photos, and event lifecycle actions from a shell using curl and an authenticated cookie jar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-oriented users use this skill to inspect and operate a real Evite account from shell commands when they need event data or write actions without running the Evite MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent live Evite account access and commands that can mutate real events.

Mitigation: Require explicit user confirmation before any write operation and verify the target event, guest, and action before execution.

Risk: Invitation sends, broadcasts, guest deletion, uploads, RSVP changes, event cancellation, and reinstatement can affect real guests.

Mitigation: Test writes only on a throwaway or low-risk event, and use blackholed or test guest addresses for send and broadcast checks.

Risk: The cookie jar contains an authenticated Evite session.

Mitigation: Create the jar with restrictive permissions, keep it protected, and remove it after use.

Risk: Two documented write bodies are marked as assumed rather than fully verified.

Mitigation: Treat private guest messages and invitation sends as higher-risk operations and review their request body and recipient impact before use.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [Evite website](https://www.evite.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied Evite credentials, a protected cookie jar, curl, awk, and jq for the documented workflows.]

## Skill Version(s):

0.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
