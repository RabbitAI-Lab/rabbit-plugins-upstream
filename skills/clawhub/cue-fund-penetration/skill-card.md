## Description:

Analyzes disclosed holdings of Chinese public-fund portfolios to identify overlapping stocks, sector concentration, and investment-style exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors, financial advisers, and fund researchers use the skill to compare public-fund holdings, spot duplicated exposures, and prepare portfolio concentration reports. Analysis relies on disclosed holdings rather than live positions or forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs or updates a third-party runner before analysis.

Mitigation: Review the runner code and changes before executing or updating it; avoid optional sudo dependency installs unless needed.

Risk: Local Cue API credentials could be exposed by shell commands or chat messages.

Mitigation: Keep the API key out of chat and logs; use environment or platform secret handling where available.

Risk: Portfolio details are sent to a hosted service, and disclosed holdings may be incomplete or stale.

Mitigation: Use the service only when comfortable sharing the query; check the report's disclosure date and underlying sources before making investment decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-fund-penetration)
- [Cue runner repository referenced by the skill](https://github.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-fund-penetration)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown portfolio diagnostic report with a link to the original Cue report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fund holdings, stock overlap, sector and style exposure, concentration assessment, suggested adjustments, sources, and the disclosure date when available.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
