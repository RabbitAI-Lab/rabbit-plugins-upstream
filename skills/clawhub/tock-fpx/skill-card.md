## Description:

Helps agents query Tock venues, availability, and a signed-in user's reservations through browser-backed shell commands without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this read-only skill to find restaurants, inspect venue availability, and review their own Tock reservations from a shell. Reservation and account details require a signed-in browser tab; the skill cannot book or cancel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in reservation and profile queries may reveal reservation history, names, and email addresses in terminal output, temporary files, logs, or transcripts.

Mitigation: Use public venue and availability queries without signing in when possible; limit access to and retention of signed-in query results.

Risk: Browser-backed access requires trusting the paired browser bridge.

Mitigation: Install the bridge only if comfortable with browser-backed access to exploretock.com, and review the extension before pairing.

## Reference(s):

- [Tock FPX release on ClawHub](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Request examples](references/requests.md)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; signed-in reservation queries can expose personal account details.]

## Skill Version(s):

1.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
