## Description:

Search Home Depot, pull full item detail and page through review bodies as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and retail data teams use this skill to search Home Depot products, retrieve full item detail, and page through customer reviews for price monitoring, catalog enrichment, and review mining.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls require SCAVIO_API_KEY, and exposing the key could leak access to paid API usage.

Mitigation: Load SCAVIO_API_KEY from the environment or a secret store and avoid including it in source code, logs, or shared transcripts.

Risk: Home Depot API requests consume credits, including empty search pages and invalid review pages.

Mitigation: Set an explicit page budget before looping, use documented fixed page sizes, and stop review pagination at total_pages.

Risk: Using the optional Scavio SDK introduces ordinary dependency supply-chain considerations.

Mitigation: Prefer direct HTTPS examples when possible, or install the SDK in a virtual environment with normal dependency hygiene.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/home-depot-product-data)
- [Scavio Home Depot Search Documentation](https://scavio.dev/docs/home-depot-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=home-depot-product-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=home-depot-product-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-oriented API examples and bash, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The referenced API returns structured JSON for product search, item detail, and paginated reviews.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
