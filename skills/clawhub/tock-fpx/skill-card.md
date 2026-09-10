## Description:

Query Tock restaurant discovery, venue availability, and signed-in reservation history from a shell using the fpx CLI through the user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Tock metros, restaurants, venue availability, and signed-in reservation history in scripts without running the Tock MCP server. It supports read-only discovery and verification workflows; booking and cancellation remain on exploretock.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route requests through a signed-in browser session and return private Tock reservation or profile data.

Mitigation: Use a dedicated browser profile when possible, pair the bridge only for exploretock.com, and run reservation or profile commands only when that private data is intentionally needed.

Risk: Authenticated responses may be kept in shared or predictable temporary files by example workflows.

Mitigation: Avoid retaining authenticated responses in shared temporary paths; delete private outputs promptly and restrict file permissions when saving them.

Risk: A bot challenge, sign-in interstitial, or GraphQL error response could be mistaken for valid Tock data.

Mitigation: Check GraphQL errors and response shape before parsing results or reporting reservation state.

## Reference(s):

- [Tock request recipes](references/requests.md)
- [Redux slice extraction helper](references/extract-redux-slice.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflows; authenticated reservation requests may expose private account data.]

## Skill Version(s):

0.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
