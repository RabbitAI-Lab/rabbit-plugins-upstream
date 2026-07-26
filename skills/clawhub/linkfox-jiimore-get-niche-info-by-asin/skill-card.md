## Description: <br>
Analyzes Amazon niche market data for a reference ASIN, including competitive intensity, brand concentration, new product success, demand, and market opportunity metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, marketplace analysts, and ecommerce agents use this skill to evaluate the niche segments associated with a known ASIN across supported US, JP, and DE marketplaces. It helps summarize demand, competition, brand concentration, pricing, advertising, and launch-success signals before further market analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound API calls and may use environment-provided gateway and session settings. <br>
Mitigation: Review the configured gateway URL, API credentials, and session-related environment variables before installation or execution. <br>
Risk: The skill stores full analysis responses locally, which may include task-specific market research data. <br>
Mitigation: Use it only in workspaces where local result storage is acceptable, and review cache and output paths before sharing or retaining generated files. <br>
Risk: The skill includes feedback-reporting behavior separate from the market analysis API. <br>
Mitigation: Review the feedback behavior and constrain or disable use according to user consent and workspace policy. <br>


## Reference(s): <br>
- [API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info-by-asin) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell commands, saved JSON response files, and tabular summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ASIN, supports US, JP, and DE marketplaces, consumes LinkFox credits, caches matching requests for 24 hours, and persists full API responses locally.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
