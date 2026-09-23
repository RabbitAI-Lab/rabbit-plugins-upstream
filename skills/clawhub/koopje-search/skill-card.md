## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping agents use this skill to find, compare, price, and inspect Belgian second-hand marketplace listings and auction lots through the koopje.ai API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The search-focused skill documents endpoints that can save items and create, publish, remove, or renew public listings.

Mitigation: Require clear, case-by-case user approval before using saved-listing or own-listing mutation endpoints; prefer read-only search, similar, contents, and stats endpoints unless the user explicitly requests account changes.

Risk: The skill requires a koopje.ai API key.

Mitigation: Install only if the user trusts koopje.ai with the key; store KOOPJE_API_KEY as a secret and do not reveal it in commands or responses.

## Reference(s):

- [koopje.ai API reference](references/api.md)
- [koopje.ai API](https://koopje.ai)
- [koopje.ai agent-readable docs](https://koopje.ai/llms.txt)
- [Koopje Search on ClawHub](https://clawhub.ai/antarcticaice/skills/koopje-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with API request examples and listing summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KOOPJE_API_KEY for authenticated koopje.ai API calls.]

## Skill Version(s):

1.0.12 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
