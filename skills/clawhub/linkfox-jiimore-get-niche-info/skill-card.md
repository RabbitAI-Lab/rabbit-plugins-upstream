## Description: <br>
Queries Jiimore data for Amazon niche market intelligence, including market metrics, reviews, competition, pricing, inventory, and growth trends for a supplied niche ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon marketplace sellers and ecommerce analysts use this skill to retrieve and summarize Jiimore niche-market intelligence for a known nicheId in the US, Japan, or Germany marketplaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and may make paid Jiimore API calls. <br>
Mitigation: Confirm credential use and expected credit cost before running; avoid repeated calls without user approval and use the built-in cache where appropriate. <br>
Risk: Full market-data responses are persisted to local linkfox session and cache files. <br>
Mitigation: Run the skill only in an appropriate workspace and periodically delete generated linkfox data or cache files when the market data is sensitive. <br>
Risk: Security evidence flags remote onboarding installation behavior and automatic feedback reporting for review. <br>
Mitigation: Review or remove the onboarding download path and feedback-reporting behavior before deploying the skill in controlled environments. <br>


## Reference(s): <br>
- [Jiimore niche market API reference](references/api.md) <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses or saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key; full responses are persisted under linkfox session data, and responses over 8 KB are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
