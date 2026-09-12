## Description:

Retrieves traceable keyword, SERP, trend, ranked-keyword, traffic, competitor, GEO, and backlink evidence through the SignalDig SEO Data MCP for evidence-only SEO research and scoped market comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, SEO analysts, and developers use this skill to request scoped, traceable SEO demand-signal research for keywords, domains, competitors, AI-search visibility, backlinks, ranked keywords, and traffic estimates. It supports evidence review and market comparison, but leaves final prioritization decisions to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted keywords and domains are sent to SignalDig for analysis.

Mitigation: Use the skill only when an external SEO data service is intended, and avoid submitting sensitive or confidential targets.

Risk: A SignalDig API key could be exposed if hardcoded in local MCP configuration or committed to a repository.

Mitigation: Use a dedicated, revocable API key through environment-variable or client secret support, and keep local MCP configuration out of version control.

Risk: Unavailable tools or invalid credentials could lead to unsupported SEO claims if the workflow is bypassed.

Mitigation: Stop when SignalDig tools are unavailable or authentication fails; do not simulate metrics, rankings, evidence IDs, or source URLs.

Risk: SEO signals may be mistaken for final prioritization decisions.

Mitigation: Separate observed evidence from interpretation and keep final SEO prioritization decisions with the user.

## Reference(s):

- [SEO Research Functional Contract](references/mcp-contract.md)
- [Setup Guide: Connect the SignalDig SEO MCP Server](references/setup-guide.md)
- [SignalDig](https://signaldig.com/)
- [Connect SignalDig](https://signaldig.com/agent-setup)
- [ClawHub Skill Page](https://clawhub.ai/jerrykik/skills/research-seo-signals)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown evidence reports with concise observations, evidence references, limitations, and optional setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected SignalDig SEO Data MCP capability and a valid API key; live results must be cited from tool output.]

## Skill Version(s):

1.8.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
