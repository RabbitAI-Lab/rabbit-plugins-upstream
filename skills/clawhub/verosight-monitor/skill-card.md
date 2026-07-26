## Description: <br>
Verosight Monitor helps agents use the Verosight API for social media intelligence, cyber monitoring, sentiment analysis, trend detection, influencer identification, bot detection, and report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jrrqd](https://clawhub.ai/user/jrrqd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to configure Verosight authentication, query social and news monitoring endpoints, inspect sentiment and trend signals, identify influential or suspicious accounts, and generate investigation reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, account identifiers, and monitoring queries are sent to Verosight. <br>
Mitigation: Use this skill only when Verosight is an approved external monitoring provider and avoid sending confidential investigation terms or private personal data unless authorized. <br>
Risk: API credentials and JWT tokens can be exposed if passed or logged carelessly. <br>
Mitigation: Prefer environment variables or secure secret handling for Verosight credentials and avoid embedding production API keys in prompts, command history, or shared reports. <br>


## Reference(s): <br>
- [Verosight Monitor on ClawHub](https://clawhub.ai/jrrqd/skills/verosight-monitor) <br>
- [Verosight API](https://verosight.com) <br>
- [Verosight Documentation](https://verosight.com/docs) <br>
- [Sentiment Analysis Workflow](references/sentiment-workflow.md) <br>
- [PDF Report Generation Template](references/pdf-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API examples, shell commands, JSON response shapes, and report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl commands, authentication setup, endpoint parameters, monitoring workflow steps, and report-generation snippets.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
