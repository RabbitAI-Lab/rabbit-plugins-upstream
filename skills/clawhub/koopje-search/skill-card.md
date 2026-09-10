## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, compare, price, and inspect Belgian second-hand listings and auction lots through the koopje.ai API. Agents can return listing summaries with prices, locations, sources, and links, or deepen results with detailed listing contents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes account-changing actions including saving, removing, creating, publishing, and renewing listings.

Mitigation: Require explicit user confirmation before performing any account-changing action and limit routine use to read-only search, similar, answer, contents, and stats endpoints.

Risk: The required KOOPJE_API_KEY may authorize more than search-only access.

Mitigation: Treat the API key as sensitive, avoid exposing it in logs or responses, and install the skill only when the user accepts the associated account permissions.

## Reference(s):

- [koopje.ai API reference](artifact/references/api.md)
- [ClawHub skill page](https://clawhub.ai/antarcticaice/skills/koopje-search)
- [koopje.ai agent-readable docs index](https://koopje.ai/llms.txt)
- [koopje.ai integration guide](https://koopje.ai/koppelen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance]

**Output Format:** [Markdown with inline shell commands, API request examples, and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Belgian marketplace listing URLs, prices, locations, source names, citations, and account-action recommendations requiring confirmation.]

## Skill Version(s):

1.0.7 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
