## Description:

Helps agents search Etix events, venues, and performers and retrieve event or venue details using shell calls through a paired browser tab instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to discover public Etix event and venue information from a shell without running an Etix MCP server. It covers search and detail lookups, not ticket purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access uses a third-party browser bridge with persistent pairing and Etix site access.

Mitigation: Review the bridge before installation, verify the extension archive checksum or build from source, and pair only the intended Etix profile.

Risk: Example commands store event searches and page contents in local temporary files.

Mitigation: Treat temporary outputs as local search traces and delete them when no longer needed.

## Reference(s):

- [Etix consumer endpoints and extraction examples](references/etix-endpoints.md)
- [Etix dataLayer extraction helper](references/extract-datalayer.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [FetchProxy extension information](https://github.com/chrischall/fetchproxy#extension)
- [Etix FPX skill release](https://clawhub.ai/chrischall/skills/etix-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Code]

**Output Format:** [Markdown with shell and JavaScript examples; Etix responses may be JSON or HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event and venue detail may require extracting structured data from HTML.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
