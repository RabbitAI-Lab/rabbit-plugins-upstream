## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find, compare, and price Belgian second-hand listings, thrift-store items, car listings, and auction lots through the koopje.ai API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents saved-listing and own-listing endpoints that can change account state or publish public listings.

Mitigation: Require explicit user confirmation before saving, removing, renewing, drafting, publishing, or managing own listings.

Risk: The skill requires a koopje.ai API key and may use location or conversation details during searches.

Mitigation: Keep the API key in KOOPJE_API_KEY and avoid sending precise location or sensitive conversation history unless needed for the request.

Risk: Search results, prices, and auction availability may be incomplete or stale.

Mitigation: Report only API-returned listings, include source, price, location, and links, and surface API errors or empty result sets without inventing listings.

## Reference(s):

- [koopje.ai /v1 API reference](references/api.md)
- [koopje.ai API base](https://koopje.ai)
- [Agent-readable koopje.ai documentation](https://koopje.ai/llms.txt)
- [koopje.ai integration templates](https://koopje.ai/koppelen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API examples and concise result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KOOPJE_API_KEY; account-changing actions should be confirmed before execution.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
