## Description:

Helps agents find public Etix events, venues, and performers and retrieve event and venue details through a paired browser using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can search public Etix listings and inspect event or venue details from an agent or shell without running the Etix MCP server. The skill is for anonymous discovery, not purchases or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use requires installing a CLI and browser extension and pairing a browser tab.

Mitigation: Install only if comfortable with both components; verify the extension package or build from source, and limit pairing to etix.com.

Risk: A successful request may return a bot-check page instead of event details.

Mitigation: Check the returned page before extracting or reporting event information.

Risk: Discovery results could be mistaken for permission to buy tickets or act on an account.

Mitigation: Keep use limited to anonymous event discovery; do not perform purchases or account actions.

## Reference(s):

- [Etix FPX ClawHub release](https://clawhub.ai/chrischall/skills/etix-fpx)
- [Etix consumer endpoint guide](references/etix-endpoints.md)
- [Etix dataLayer extraction helper](references/extract-datalayer.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and public event data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only event discovery; no ticket purchases or account actions.]

## Skill Version(s):

1.1.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
