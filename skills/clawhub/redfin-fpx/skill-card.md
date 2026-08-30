## Description:

Query Redfin from a shell with the fpx CLI to resolve locations, search listings, read property details, market trends, rentals, climate risk, photos, and signed-in saved Redfin data through a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce fpx commands and parsing guidance for Redfin search, property detail, market trend, rental, climate risk, photo, saved-home, and saved-search lookups. It is intended for workflows that need Redfin data through a paired browser session instead of a running MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill can access account-specific Redfin saved homes and saved searches when the paired browser tab is signed in.

Mitigation: Use the saved-homes and saved-searches examples only when intentionally allowing the agent to read that Redfin account data.

Risk: The paired browser bridge can retrieve Redfin data visible to the active browser session.

Mitigation: Pair only the Redfin fpx profile, keep browser site access scoped to redfin.com, and review commands before execution.

Risk: Redfin may reject a request or substitute a nearby indexed region, which can make results misleading.

Mitigation: Check resultCode, errorMessage, and serviceRegionName before trusting returned listing or market data.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub skill page: redfin-fpx](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires @fetchproxy/cli, Transporter extension pairing, and a browser tab with access to redfin.com; saved homes and saved searches require a signed-in Redfin session.]

## Skill Version(s):

0.11.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
