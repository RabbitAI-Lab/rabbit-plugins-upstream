## Description:

Find public Etix events, venues, and performers and retrieve event and venue details with fpx through a paired browser tab, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can look up public Etix events, venues, and performers and extract event or venue details from a shell without running the Etix MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The globally installed CLI and browser extension require trust in their distribution sources.

Mitigation: Review the npm package and extension provenance before installation; verify the extension download or build it from source.

Risk: The paired browser bridge can access sites permitted by its profile.

Mitigation: Keep the fpx profile limited to etix.com and use the skill only for public, anonymous discovery.

Risk: Example commands may overwrite fixed filenames under /tmp.

Mitigation: Choose different output paths when those temporary filenames contain data you need to keep.

Risk: Ticket purchases or authenticated account actions fall outside this lookup skill.

Mitigation: Do not use this skill for purchases or authenticated Etix account actions.

## Reference(s):

- [Etix endpoint and extraction reference](references/etix-endpoints.md)
- [Etix dataLayer extraction helper](references/extract-datalayer.mjs)
- [ClawHub release listing](https://clawhub.ai/chrischall/skills/etix-fpx)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes steps for interpreting JSON search results and extracting event or venue details from HTML.]

## Skill Version(s):

1.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
