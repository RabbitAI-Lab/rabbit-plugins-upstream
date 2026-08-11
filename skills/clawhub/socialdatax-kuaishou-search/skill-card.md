## Description:

Helps agents search Kuaishou/Kwai works for keyword discovery, content research, competitor analysis, and trend scanning using SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Kuaishou/Kwai public-content search, keyword discovery, content research, competitor analysis, and trend scanning. The agent can return traceable result summaries with content IDs, URLs, authors, visible counts, and publish times when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and API-key-backed requests are sent to the SocialDataX service.

Mitigation: Use the skill only for Kuaishou research that is appropriate to send to SocialDataX, and provide the SOCIALDATAX_API_KEY intentionally through the runtime environment.

Risk: The direct CLI path uses npm to fetch the declared socialdatax-skills package.

Mitigation: Install and run the CLI only in environments where fetching that package is acceptable.

Risk: Paging through search results can consume API balance or credits.

Mitigation: Set practical page or item limits, monitor balance, and avoid repeated retries when an insufficient-balance response is returned.

Risk: Requests outside read-only Kuaishou search could exceed the skill's stated boundary.

Mitigation: Keep usage to public-content search and do not use this skill for login, posting, liking, commenting, or account changes.

## Reference(s):

- [SocialDataX API access and homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-search)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI examples and JSON search-result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports keyword search, optional pagination tokens, page limits, max-item limits, and traceable Kuaishou result fields such as photo IDs and share URLs.]

## Skill Version(s):

0.1.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
