## Description:

Helps agents retrieve and interpret Google Trends interest, regional demand, related queries, and Trending Now data through Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heocoi](https://clawhub.ai/user/heocoi)

### License/Terms of Use:

MIT-0

## Use Case:

People researching search demand and trending topics can compare up to five keywords across Google search properties, regions, and time periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify access token exposure.

Mitigation: Keep APIFY_TOKEN secret and avoid including it in shared commands or logs.

Risk: Apify usage may incur charges.

Mitigation: Review Apify billing and expected usage before running queries.

Risk: Private search terms are sent to Apify.

Mitigation: Avoid sensitive queries unless sharing them with Apify fits the use case.

## Reference(s):

- [Google Trends Apify Actor](https://apify.com/heocoi/google-trends-api)
- [ClawHub skill release](https://clawhub.ai/heocoi/skills/google-trends)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Text or Markdown summaries of JSON trend results, with optional curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trend values are relative (0–100); compare keywords within the same query.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
