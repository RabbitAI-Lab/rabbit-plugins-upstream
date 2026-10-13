## Description:

Guides agents to query Zillow listings, property details, histories, market reports, and optionally a user's saved homes and searches through the fpx CLI and a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve US Zillow listing, property, and market information from a shell without running the Zillow MCP server. With a signed-in browser tab, they can also access the user's saved searches and homes.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Pairing the browser extension and CLI permits requests through an open Zillow tab.

Mitigation: Verify the extension and CLI source before pairing, and only pair if this browser access is acceptable.

Risk: Saved homes and searches can expose personal information in terminal output or temporary files.

Mitigation: Run saved-data commands intentionally and protect or remove any resulting output files.

## Reference(s):

- [Zillow via fpx on ClawHub](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [Zillow page recipes](references/pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and data-extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce JSON extracted from Zillow pages; saved-data results depend on the user's signed-in browser tab.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
