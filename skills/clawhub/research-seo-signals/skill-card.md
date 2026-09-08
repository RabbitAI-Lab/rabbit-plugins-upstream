## Description:

Retrieve traceable keyword, SERP, trend, ranked-keyword, traffic, competitor, GEO, and backlink evidence through the SignalDig SEO Data MCP for evidence-only SEO research and scoped market comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and SEO analysts use this skill to retrieve traceable demand-signal evidence for keywords, domains, competitors, GEO visibility, backlinks, ranked keywords, and traffic estimates through a connected SignalDig MCP server. It is intended to organize observed evidence for research, not to make final prioritization decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a live SignalDig MCP server and API key, so installation alone does not provide data access.

Mitigation: Configure the MCP endpoint separately, store the API key outside project files, and stop rather than simulate results when the required tools are unavailable.

Risk: Live SEO requests may consume SignalDig service quota or credits.

Mitigation: Keep tool approvals enabled, review requested scopes before execution, reuse prior results when appropriate, and request only the data families needed for the task.

Risk: SEO signals can be incomplete or unsuitable for automatic final prioritization decisions.

Mitigation: Separate observed evidence from interpretation, cite only returned evidence, disclose partial coverage, and leave final prioritization to the user.

## Reference(s):

- [SignalDig](https://signaldig.com/)
- [SignalDig SEO MCP Setup Guide](references/setup-guide.md)
- [SEO Research Functional Contract](references/mcp-contract.md)
- [ClawHub Skill Page](https://clawhub.ai/jerrykik/skills/research-seo-signals)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown evidence reports with cited request and result details when MCP data is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected SignalDig SEO Data MCP server and SignalDig API key; live requests may consume service quota or credits.]

## Skill Version(s):

1.8.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
