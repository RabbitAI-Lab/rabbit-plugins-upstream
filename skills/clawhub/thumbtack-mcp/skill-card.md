## Description:

Query thumbtack.com from a shell to search local service pros by trade and ZIP code and read pro profiles with ratings, reviews, credentials, business hours, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose shell-based Thumbtack queries, parse public search and profile pages, and extract local service provider data without an account or API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes anonymous network requests to Thumbtack and processes public local business profile data.

Mitigation: Use it only where collecting and processing public Thumbtack data is appropriate for the user's task, site terms, and privacy expectations.

Risk: Thumbtack page shapes and GraphQL responses can vary or return errors even with HTTP 200 responses.

Mitigation: Check parsed output and GraphQL errors before relying on results, and handle missing prices, credentials, or profile fields as documented.

Risk: Search and profile extraction are read-only but can still surface stale or incomplete public business information.

Mitigation: Treat extracted provider data as a starting point and verify important details against the live Thumbtack profile before use.

## Reference(s):

- [Thumbtack Discovery Recipes](artifact/references/discovery.md)
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/thumbtack-mcp)
- [Thumbtack](https://www.thumbtack.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON/jq extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only request recipes and parsed public Thumbtack data; does not book, contact, or write to Thumbtack accounts.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
