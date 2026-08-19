## Description:

美客多选品数据 helps agents query and analyze Mercado Libre product, catalog, keyword, category trend, seller, review, exchange-rate, and plan-usage data through the LinkFox gateway across Mexico, Brazil, Argentina, Chile, and Colombia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and their agents use this skill to research Mercado Libre products, categories, keywords, sellers, reviews, exchange rates, and LinkFox plan usage before making product-selection decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use LinkFox account credentials and send onboarding data to LinkFox services.

Mitigation: Prefer self-service API-key setup, store credentials only in the documented environment variables, and avoid sharing keys or raw authentication output in prompts.

Risk: The onboarding workflow can create payment orders and paid Mercado Libre tool calls can consume account credits.

Mitigation: Confirm billing actions and paid API calls with the user before proceeding, and check plan usage or returned cost fields when cost expectations are unclear.

Risk: Full query responses are saved locally and may contain sensitive business or account data.

Mitigation: Run the skill in a private workspace, avoid shared or repository workspaces for sensitive research, and clean the local linkfox output and cache when the data is no longer needed.

Risk: Marketplace analytics results may be incomplete, empty, or unsuitable for unsupported business conclusions.

Mitigation: Present returned fields directly, preserve important source labels, and avoid extrapolating recommendations that are not supported by the returned data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mercado-product-selection)
- [Mercado Libre Product Selection API reference](references/api.md)
- [Mercado XP-MCP Tool Reference](references/mercado-tool-reference.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, shell commands, and JSON API results saved to local files with stdout summaries for large responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses environment-based LinkFox credentials, writes full query responses under a local linkfox session directory, and caches repeated calls for 24 hours.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
