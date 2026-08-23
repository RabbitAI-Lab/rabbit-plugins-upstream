## Description:

An Apple App Store API alternative on fetcher.sh for searching iOS apps and bundles, fetching details, reviews, similar apps, and developer catalogs across country storefronts without Apple Developer Program membership.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to integrate paid App Store data lookups into workflows for app discovery, ASO research, competitor monitoring, localized storefront comparison, and developer catalog review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, app identifiers, and API usage are sent to fetcher.sh.

Mitigation: Use the skill only when the user accepts sharing those requests with fetcher.sh, and avoid sending confidential or unnecessary identifiers.

Risk: Paid calls can consume prepaid credits or trigger x402 payment.

Mitigation: Confirm payment posture before making paid requests and configure API keys or MCP authorization headers only for trusted environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/app-store-api)
- [Server-resolved GitHub source](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/app-store)
- [Full agent setup](https://appstore.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://appstore.fetcher.sh/openapi.json)
- [Condensed catalog](https://appstore.fetcher.sh/llms.txt)
- [Site](https://appstore.fetcher.sh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to make HTTP GET requests or configure an MCP server for the App Store API.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
