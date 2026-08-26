## Description:

Google Search provides agent-facing guidance for using fetcher.sh to retrieve Google search results as clean JSON with search operators, pagination, language and country scoping, and prepaid or x402 payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and call a paid Google search-results API, including examples for site-restricted searches, filetype searches, exact phrases, localized results, and MCP setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid search requests and top-up actions may incur costs.

Mitigation: Review pricing and payment method before enabling the skill, and monitor usage after deployment.

Risk: MCP configuration can include a Bearer key.

Mitigation: Store the key as a secret, avoid committing it, and rotate it if exposed.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/google-search)
- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/google-search)
- [Full agent setup](https://google.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://google.fetcher.sh/openapi.json)
- [Condensed catalog](https://google.fetcher.sh/llms.txt)
- [Service site](https://google.fetcher.sh)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes paid API usage, authentication options, MCP configuration, error codes, and external API references.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
