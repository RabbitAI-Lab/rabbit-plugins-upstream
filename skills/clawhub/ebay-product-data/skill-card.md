## Description:

Search eBay live and sold listings, read a single listing in full, and retrieve a seller public profile card as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to research eBay market prices, compare live and sold listings, inspect listing details, and check seller profile data through Scavio's eBay endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: eBay search terms, item identifiers, and seller identifiers are sent to Scavio, and each endpoint call consumes one Scavio credit.

Mitigation: Confirm the user intends to query Scavio before calling the API, avoid sending sensitive search text, and disclose credit use for calls.

Risk: The Scavio API key can be exposed if it is pasted into source files, logs, or shared transcripts.

Mitigation: Load SCAVIO_API_KEY from an environment variable or secret store and do not commit it to source control.

Risk: Marketplace conclusions can be misleading if returned listing data is treated as complete or if API guardrails are ignored.

Mitigation: Use only API-returned prices, dates, item numbers, feedback scores, and seller names; include listing URLs and call out sold-listing dates when quoting market value.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/ebay-product-data)
- [Scavio eBay search documentation](https://scavio.dev/docs/ebay-search)
- [Scavio eBay product documentation](https://scavio.dev/docs/ebay-product)
- [Scavio eBay seller documentation](https://scavio.dev/docs/ebay-seller)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON request and response details, shell setup, and Python request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented endpoint call uses one Scavio credit and returns a structured JSON envelope.]

## Skill Version(s):

1.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
