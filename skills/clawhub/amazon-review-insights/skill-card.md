## Description: <br>
Amazon Review Insights helps agents collect and analyze Amazon product reviews through AstrMap APIs, including negative feedback, trend, statistics, and improvement insight workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sparkbayes](https://clawhub.ai/user/sparkbayes) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce sellers and their agents use this skill to create or inspect AstrMap review-analysis tasks for Amazon ASINs, retrieve completed insights, and guide product improvement or market research decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AstrMap API credentials and product or review task data are sent to AstrMap. <br>
Mitigation: Install only when this data sharing is acceptable, store the API key in CUSTOMER_INSIGHTS_API_KEY or another protected secret store, and rotate or disable the key when no longer needed. <br>
Risk: Some workflows require a desktop client logged into an Amazon buyer account and may consume AstrMap points. <br>
Mitigation: Use a dedicated Amazon buyer account, verify the desktop-client download and signature, and confirm with the user before actions that spend points or change tasks. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/sparkbayes/skills/amazon-review-insights) <br>
- [AstrMap API Reference](artifact/references/api_reference.md) <br>
- [AstrMap Desktop Client Security Guide](artifact/references/security.md) <br>
- [AstrMap website](https://www.astrmap.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CUSTOMER_INSIGHTS_API_KEY for authenticated AstrMap API actions; task creation and incremental fetch workflows may require the AstrMap desktop client.] <br>

## Skill Version(s): <br>
1.2.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
