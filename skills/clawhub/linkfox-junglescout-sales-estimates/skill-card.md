## Description: <br>
Queries Jungle Scout ASIN sales estimates through LinkFox to return daily estimated Amazon unit sales and last known price across 10 marketplaces for a requested date range. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, e-commerce analysts, and developers use this skill to estimate daily sales for a specific ASIN, monitor competitors, evaluate demand, and summarize historical sales trends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and sends ASIN/date queries plus session metadata to LinkFox services. <br>
Mitigation: Install only when that data sharing is acceptable, use a dedicated or scoped API key where possible, and avoid including sensitive business context in query text. <br>
Risk: The security summary notes mismatched local data storage behavior and retained full results. <br>
Mitigation: Review the generated LinkFox data directory after use, remove result files that should not be retained, and limit workspace access to authorized users. <br>
Risk: A configured LINKFOX_TOOL_GATEWAY can change the destination that receives tool requests. <br>
Mitigation: Leave LINKFOX_TOOL_GATEWAY unset unless the destination is explicitly trusted. <br>
Risk: Automatic feedback-reporting instructions may send user comments or task context to a separate LinkFox feedback service. <br>
Mitigation: Review or disable feedback reporting before use if that transfer is not acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-sales-estimates) <br>
- [Jungle Scout ASIN sales estimate API reference](references/api.md) <br>
- [LinkFox API key guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses, saved JSON result files, tables, trend summaries, and optional shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key, consumes 63.75 credits per call, supports one ASIN per request, requires endDate before the current date, and may cache results for 24 hours.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
