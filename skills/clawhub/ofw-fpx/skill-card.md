## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal from a shell with the fpx CLI and curl, using a signed-in browser session to capture the bearer token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to access OurFamilyWizard account data and perform account actions from shell scripts or machines without the ofw-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes, deletions, uploads, and visibility changes affect shared family records without a built-in confirmation step.

Mitigation: Prefer read-only or draft-only use when possible, and require explicit approval after reviewing each consequential change.

Risk: The captured bearer token grants account access, and browser pairing persists across invocations.

Mitigation: Protect the captured token and revoke browser pairing when finished.

Risk: Reading an unread message can create a visible read receipt.

Mitigation: Consider this side effect before fetching unread message details.

## Reference(s):

- [requests.md](artifact/references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy extension reference](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands, curl requests, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.22.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
