## Description: <br>
Generates a structured A-share daily market review from public akshare data, covering major indices, market sentiment, sector leaders and laggards, limit-up tiers, and Dragon-Tiger Board activity without requiring an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tangbinbinm](https://clawhub.ai/user/tangbinbinm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to produce a concise Markdown recap of the latest or requested A-share trading day from public market data. It is intended for factual market reporting, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake factual market summaries for investment advice. <br>
Mitigation: Keep reports limited to observed market data, avoid buy or sell recommendations, and include the required investment-risk disclaimer. <br>
Risk: Public akshare data sources may be unavailable, delayed, or incomplete. <br>
Mitigation: Report unavailable sections explicitly from the script errors and do not fabricate missing figures. <br>
Risk: Broad stock-market prompts may invoke the skill and fetch public A-share data. <br>
Mitigation: Make clear that the report uses public data and that users should independently verify important financial information. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/tangbinbinm/skills/a-share-daily-review) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown report generated from a local JSON data collection script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches public A-share market data through akshare; sections tolerate source failures and report missing data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
