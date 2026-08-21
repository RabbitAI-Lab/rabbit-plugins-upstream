## Description:

Searches Seerfar market keyword data for Ozon and available Wildberries rows, filtering marketplace search terms by search volume, growth, product and seller counts, competition, price, sales, conversion concentration, and related market metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, e-commerce analysts, and agents use this skill to discover and rank Ozon search terms by market demand, competition, pricing, sales, and conversion metrics. It is suited for keyword research, blue-ocean term discovery, and market opportunity analysis rather than SKU, seller, or category-tree research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags use of a LinkFox API key and possible printing of API keys during onboarding.

Mitigation: Treat any printed API key as a secret, prefer obtaining keys through the official LinkFox website, and avoid sharing credentials in general chat.

Risk: The security review flags phone login and payment flows for purchasing credits.

Mitigation: Use the in-skill onboarding flow only intentionally, prefer official LinkFox payment pages when possible, and avoid sharing SMS codes unless deliberately using that flow.

Risk: The security review flags persistent local storage of full market-search responses.

Mitigation: Install only if local linkfox session folders are acceptable for the workspace, and review stored response files for sensitive or business-confidential query data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-market-keyword-search)
- [Seerfar Ozon market keyword search API reference](references/api.md)
- [Authentication and credits onboarding guide](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, JSON API responses, local JSON data files, and shell commands for API or onboarding flows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full market-search responses are persisted to local linkfox session folders; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
