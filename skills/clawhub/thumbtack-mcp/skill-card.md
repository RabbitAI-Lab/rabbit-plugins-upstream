## Description:

Find local Thumbtack service professionals by trade and ZIP code, and read public profiles, ratings, reviews, credentials, hours, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can look up local service professionals and inspect public Thumbtack profile details without logging in or running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookups send anonymous outbound requests to Thumbtack and parse public page data.

Mitigation: Review this access before use; do not add account cookies, credentials, or private user data without separate review.

Risk: Pricing and ratings may differ between search results and profiles, and some professionals list no numeric price.

Mitigation: Check the current profile and handle missing prices rather than assuming a quoted amount.

## Reference(s):

- [Thumbtack skill release](https://clawhub.ai/chrischall/skills/thumbtack-mcp)
- [Thumbtack discovery recipes](references/discovery.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups of publicly available Thumbtack data]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
