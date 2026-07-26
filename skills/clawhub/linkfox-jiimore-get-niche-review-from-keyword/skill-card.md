## Description: <br>
Guides an agent to query LinkFox/Jiimore Amazon niche-market review data by keyword and summarize consumer sentiment, pain points, review topics, and demand signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, e-commerce operators, and market researchers use this skill to retrieve niche-level review sentiment for a keyword and identify customer pain points, positive themes, and product improvement opportunities. It is intended for supported Amazon marketplaces and should not be used for individual ASIN review analysis or unrelated advertising, pricing, or sales-forecasting tasks. <br>

### Deployment Geography for Use: <br>
Global, with marketplace data limited to Amazon US, JP, and DE. <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends keywords, API credentials, and session or app metadata to LinkFox-configured endpoints. <br>
Mitigation: Use only trusted LinkFox gateway settings, avoid sensitive keywords unless necessary, and confirm the API key is intended for this data-sharing context. <br>
Risk: The skill stores full API responses and cached responses locally, which may retain market research data longer than expected. <br>
Mitigation: Review saved LinkFox data locations after use and delete response or cache files that should not remain in the workspace. <br>
Risk: Onboarding and feedback flows may involve remote downloads or submissions outside the main review-query workflow. <br>
Mitigation: Require explicit user approval before any onboarding download or feedback submission. <br>
Risk: Each API call consumes LinkFox credits, and repeated or exploratory queries may create unexpected cost. <br>
Mitigation: Explain credit use before additional searches and reuse cached same-parameter results when appropriate. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-review-from-keyword) <br>
- [Jiimore Amazon Niche Review API Reference](references/api.md) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell commands, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved locally as JSON; small responses may also print in full, while larger responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
