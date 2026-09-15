## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, compare, price, and inspect Belgian second-hand listings, auction lots, and similar items through the koopje.ai API. It is suited for deal-finding workflows that need prices, locations, sources, listing links, and cited answers from real listings.

### Deployment Geography for Use:

Global, focused on Belgian marketplace listings.

## Known Risks and Mitigations:

Risk: The skill requires a real koopje.ai API key for authenticated API access.

Mitigation: Install it only where the key can be stored securely and avoid exposing the key in prompts, logs, or shared command output.

Risk: The API includes account-changing and public listing actions, including saving, removing, publishing, renewing, or removing listings.

Mitigation: Require explicit user confirmation before any non-search action that changes saved listings, drafts, or public ads.

Risk: Location filters can use raw latitude and longitude.

Mitigation: Prefer postcode-level location filters when possible and request raw coordinates only when the task requires finer location matching.

## Reference(s):

- [koopje.ai /v1 API reference](artifact/references/api.md)
- [koopje.ai API](https://koopje.ai)
- [koopje.ai agent-readable docs](https://koopje.ai/llms.txt)
- [koopje.ai integration templates](https://koopje.ai/koppelen)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a KOOPJE_API_KEY environment variable for authenticated koopje.ai API access.]

## Skill Version(s):

1.0.9 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
