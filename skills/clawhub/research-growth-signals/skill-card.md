## Description:

Retrieve traceable public social and SEO signals through SignalDig's unified research tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to turn social or SEO growth-research questions into bounded SignalDig analyses. It helps collect and summarize public discussions, keyword demand, SERP patterns, trends, competitors, GEO visibility, backlinks, rankings, and traffic evidence with coverage and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics, domains, URLs, and public social or SEO requests are sent to SignalDig under the user's API key.

Mitigation: Use the skill only for requests appropriate for the SignalDig account, and review SignalDig data handling expectations before sending sensitive business topics or targets.

Risk: Implicit invocation can create account usage and cost when requests match the skill's research scope.

Mitigation: Review account limits and cost expectations, and require the skill to preserve the user's requested scope instead of broadening platforms, topics, or evidence families.

Risk: Returned research may be partial or bounded by source coverage, platform limits, or failed sources.

Mitigation: Report the actual coverage and limitations from terminal SignalDig responses, and avoid describing partial evidence as exhaustive or representative.

## Reference(s):

- [SignalDig](https://signaldig.com/)
- [SignalDig Unified Research MCP Contract](references/mcp-contract.md)
- [SignalDig Connection Setup](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with concise research findings, source evidence, coverage, limitations, and analysis IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public URLs and reported metrics from terminal SignalDig responses; does not execute local code or persist hidden local data.]

## Skill Version(s):

2.1.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
