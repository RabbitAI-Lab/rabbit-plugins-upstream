## Description:

Builds a self-contained HTML dashboard summarizing market mood, sentiment, watchlists, position changes, overnight stories, and upcoming earnings from SentiSense data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and market researchers can use it to review a morning market briefing in a browser. The dashboard is informational and read-only, not a trading or investment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions include persistent dashboard pinning and replacement behavior in addition to generating a named HTML file.

Mitigation: Review the persistence and replacement steps before installation, and confirm the intended dashboard target before using them.

Risk: The security scan had incomplete coverage because some local references could not be matched to bundled files.

Mitigation: Review the skill instructions and relevant references before installation; the scan does not establish that all behavior is safe.

## Reference(s):

- [SentiSense API and skill documentation](https://sentisense.ai/skill.md)
- [SentiSense](https://sentisense.ai)
- [Stock Market Dashboard on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [HTML, Code, Guidance]

**Output Format:** [Single self-contained HTML document with inline CSS and JavaScript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static market-data snapshot; no external assets or build step.]

## Skill Version(s):

1.2.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
