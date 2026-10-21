## Description:

Helps agents search Etix events, venues, and performers and retrieve public event details through a paired browser using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up public Etix events, venues, and performers from a shell without running an MCP server. It is limited to event discovery and detail retrieval, not ticket purchases or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a browser bridge with persistent pairing to access Etix pages.

Mitigation: Install the CLI and extension only from the stated sources, verify the extension checksum or build it from source, and scope the profile to Etix discovery reads.

Risk: Browser-backed access could be used for ticket purchases or account actions outside the skill's intended scope.

Mitigation: Keep usage limited to public discovery and event detail; do not authorize purchases or account actions.

## Reference(s):

- [Etix FPX on ClawHub](https://clawhub.ai/chrischall/skills/etix-fpx)
- [Etix endpoint reference](references/etix-endpoints.md)
- [Etix dataLayer extraction helper](references/extract-datalayer.mjs)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and Etix discovery results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may be JSON; event detail is extracted from HTML.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
