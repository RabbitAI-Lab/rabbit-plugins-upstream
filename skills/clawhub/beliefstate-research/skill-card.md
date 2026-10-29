## Description:

Retrieve dated, cited investor research from BeliefState when asked about stock theses, investment themes, risks, catalysts, conflicting views or research changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antcolombo](https://clawhub.ai/user/antcolombo)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to retrieve and compare released, dated research on a company, investment theme, catalysts, risks, or changes in a view. It presents attributed claims with evidence links, dates, horizons, coverage limits, and unknowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research access may use account allowance, prepaid credit, or an explicitly authorized wallet payment; OAuth permissions and quoted costs affect the user's account.

Mitigation: Check research pricing and OAuth permissions before connecting, and set a clear spending limit for wallet payments.

Risk: External setup documentation has not been verified.

Mitigation: Review the maintained quickstart and current API contract before connecting an account or wallet.

## Reference(s):

- [BeliefState Research](https://beliefstate.ai)
- [BeliefState Agent Quickstart](https://beliefstate.ai/agent-quickstart.md)
- [BeliefState Research Catalog](https://beliefstate.ai/v1/research)
- [BeliefState OpenAPI Contract](https://beliefstate.ai/openapi.json)
- [BeliefState Ticker Discovery](https://beliefstate.ai/v1/tickers?q=NBIS)
- [BeliefState Account MCP](https://beliefstate.ai/mcp)
- [BeliefState Research Skill on ClawHub](https://clawhub.ai/antcolombo/skills/beliefstate-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research summaries with dated citations and evidence URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves attribution, distinct date types, coverage limits, freshness, and unknowns; separates investor claims from engine analysis and independently verified facts.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
