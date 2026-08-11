## Description:

Query China's official export statistics through seven DouMaoTong REST endpoints covering product dashboards, monthly trends, destination markets, growth rankings, unit-price bands, industry-chain structure, and product opportunity rankings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[findhappy7](https://clawhub.ai/user/findhappy7)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and trade analysts use this skill to retrieve China export metrics for product selection, market research, pricing reference, and destination-market analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends product or HS-code lookup requests to DouMaoTong.

Mitigation: Avoid submitting confidential product plans or sensitive trade queries unless external sharing is approved.

Risk: Free endpoints return ranked subsets, so results may not represent complete market rankings.

Mitigation: Clearly label Top N limits in responses and do not present subsets as complete lists.

Risk: The dataset is export-only, RMB-denominated, starts in January 2021, and updates monthly after China Customs releases with a typical lag.

Mitigation: State source, currency, period, coverage, and update lag when using figures for analysis.

Risk: HS-code prefixes may resolve to a different analyzable 8-digit code, and some codes may return no data.

Mitigation: Use the returned resolved HS code, explain no-data responses plainly, and do not estimate missing figures.

## Reference(s):

- [DouMaoTong](https://doumaotong.com)
- [ClawHub skill listing](https://clawhub.ai/findhappy7/skills/china-export-data)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text summaries with REST API request guidance and source attribution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [All figures should state China Customs source, RMB currency, period, and subset limits when applicable.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
