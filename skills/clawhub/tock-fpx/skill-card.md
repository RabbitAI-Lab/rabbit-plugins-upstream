## Description:

Helps agents query Tock restaurants, availability, and signed-in reservations from a browser-backed shell without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find restaurants and available reservations on Tock, or retrieve their own reservation history through a browser session. Booking and cancellation remain on Tock's website.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-backed access to a signed-in Tock session can expose account identity and reservation history.

Mitigation: Grant browser access only if comfortable with the extension and avoid sharing reservation responses.

Risk: Example commands can leave personal reservation data in temporary files or logs.

Mitigation: Avoid running sensitive examples on shared machines or saving their responses to uncontrolled logs.

## Reference(s):

- [Tock request examples](references/requests.md)
- [Redux slice extraction helper](references/extract-redux-slice.mjs)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries; signed-in results can include personal reservation details.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
