## Description:

Research app-market opportunities using Crawlora app catalogs, historical charts, live store listings, release notes, reviews, and Google Trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and product researchers use this skill to assess app niches, compare competitors, inspect app-store chart and review signals, and produce evidence-backed opportunity hypotheses with next validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and app-market queries or request bodies used with the skill.

Mitigation: Keep CRAWLORA_API_KEY in the environment, review Crawlora as a third-party API provider before use, and avoid submitting confidential business terms unless permitted.

Risk: App-store ranks, review samples, chart snapshots, and Google Trends scores can be stale, partial, or easy to over-interpret.

Mitigation: Report dates, storefronts, devices, countries, sample sizes, and missing-data flags; avoid treating ranks, review frequencies, or Trends scores as market size, revenue, installs, or causal proof.

Risk: Shell commands generated from the workflow call a third-party API endpoint.

Mitigation: Inspect commands before execution, use only the documented Crawlora route set, and stop on authentication, authorization, rate-limit, or application-code errors.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity brief with inline shell commands and evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes data freshness, sampling bounds, unknowns, assumptions, supporting and conflicting evidence, and next validation steps.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
