## Description:

Helps agents collect and summarize XHS/RedNote hot-search and keyword search results for trend research, content planning, and marketing inspiration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operations teams, brand researchers, creators, and agents use this skill to inspect XHS/RedNote hot topics, search public notes by keyword, and turn returned rankings, titles, accounts, links, and IDs into trend insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may return full XHS note URLs containing xsec_token query parameters.

Mitigation: Review outputs before sharing externally and remove tokenized query parameters when full original links are not required.

Risk: The skill depends on a SocialDataX API key and external API availability.

Mitigation: Store SOCIALDATAX_API_KEY in the agent environment, avoid embedding it in prompts or files, and treat API, network, or balance errors as operational conditions.

Risk: Trend conclusions can be incomplete because searches are constrained by returned pages, filters, and API pagination.

Mitigation: Label visible evidence separately from interpretation and avoid presenting sampled results as complete platform coverage.

## Reference(s):

- [SocialDataX skill homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-trend-insights-v2)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with CLI command examples, trend observations, and XHS result links or IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm, and SOCIALDATAX_API_KEY; search coverage is limited by API results, pagination, and selected filters.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
