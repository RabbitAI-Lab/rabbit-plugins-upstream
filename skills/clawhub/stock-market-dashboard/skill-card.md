## Description: <br>
Builds a self-contained, browser-openable HTML stock market dashboard that snapshots SentiSense market data for a morning market briefing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to generate a local, read-only market briefing dashboard from SentiSense data, including market mood, sector tone, attention shifts, options, filings, flows, story clusters, analyst moves, and earnings. The generated dashboard is a timestamped research snapshot and not an automated trading tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SentiSense API key for market-data calls. <br>
Mitigation: Use a key intended for read-only SentiSense access and avoid sharing generated files if they could expose sensitive local context. <br>
Risk: Generated dashboards are static snapshots and may become stale after generation. <br>
Mitigation: Display the generation timestamp and field freshness notes, and regenerate the dashboard before relying on current market context. <br>
Risk: Market sentiment, filings, options, and flow data could be mistaken for trading advice. <br>
Mitigation: Keep the dashboard framed as research and include the explicit not-investment-advice disclaimer required by the artifact. <br>


## Reference(s): <br>
- [SentiSense Website](https://sentisense.ai) <br>
- [SentiSense API Reference](https://sentisense.ai/skill.md) <br>
- [SentiSense API Key](https://app.sentisense.ai/get-api-key) <br>
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, guidance] <br>
**Output Format:** [Self-contained HTML with inline CSS and JavaScript, plus concise Markdown guidance when user input is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only SentiSense data calls; generated dashboards are static timestamped snapshots.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
