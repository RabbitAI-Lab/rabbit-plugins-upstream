## Description:

股海罗盘 helps agents collect A-share market, technical, capital-flow, research, and financial data, then produce historical signal-matching summaries, pattern statistics, charts, and DOCX reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunbinpy](https://clawhub.ai/user/sunbinpy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request A-share stock data collection, historical quantitative summaries, broker research cross-checks, ETF capital-flow context, charts, and shareable DOCX reports. It is positioned as a data and historical-statistics tool, not as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may expose its paid API key through local files, payment links, generated reports, or logs.

Mitigation: Treat the key as a paid credential, avoid sharing reports or logs that contain purchase links, and use a restricted environment when evaluating the skill.

Risk: The security summary reports that authenticated API traffic may use plain HTTP.

Mitigation: Install only if this transport risk is acceptable, and prefer restricted network execution until the publisher uses HTTPS for authenticated API traffic.

Risk: The security guidance flags hardcoded database credentials.

Mitigation: Review the skill before deployment and avoid using it in sensitive environments until the publisher removes hardcoded credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunbinpy/skills/gh-data)
- [Publisher profile](https://clawhub.ai/user/sunbinpy)
- [Vendor homepage](https://www.oraskl.com/ghdata-admin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown and text responses with optional Python code snippets, shell commands, charts, and DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs must present financial results as historical data and statistical references, not as investment advice or future-performance predictions.]

## Skill Version(s):

2.2.47 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
