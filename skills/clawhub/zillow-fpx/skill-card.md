## Description:

Guides agents in using the fpx CLI and a paired browser tab to retrieve Zillow listings, property details, market reports, and authorized saved items without a Zillow MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US property listings and inspect property records, histories, and market reports through a user's browser tab. With explicit authorization, they can also retrieve the user's saved searches and homes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing the CLI and browser extension gives the skill access to a Zillow browser tab.

Mitigation: Verify the extension and package source before installing, and pair only if comfortable granting that access.

Risk: A signed-in tab can expose personal saved searches and homes.

Mitigation: Fetch saved account data only when the user explicitly requests it.

Risk: Zillow sign-in redirects or bot checks may be mistaken for successful page results.

Mitigation: Check returned pages for sign-in or bot-check content before using extracted results.

## Reference(s):

- [Zillow fpx skill release](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [Zillow page and field reference](references/pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved results can include personal saved items when the user explicitly authorizes access.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
