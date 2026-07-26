## Description: <br>
Cloud browser automation via Browser Use API for AI-driven web browsing, scraping, form filling, and multi-step web tasks without local browser control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jfrux](https://clawhub.ai/user/jfrux) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to submit natural-language browser automation tasks to Browser Use's cloud API and retrieve structured task results, screenshots, status, and cost details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation tasks and target site content are sent to Browser Use's cloud service. <br>
Mitigation: Use only organization-approved data and workflows; do not submit secrets, credentials, regulated data, private internal URLs, or confidential workflows unless Browser Use is approved for that data. <br>
Risk: Cloud browser tasks can incur usage costs depending on task complexity. <br>
Mitigation: Scope tasks before submission and check account credits or task cost output when cost control matters. <br>


## Reference(s): <br>
- [Browser Use API ClawHub Skill](https://clawhub.ai/jfrux/skills/browser-use-api) <br>
- [Browser Use API Tasks Endpoint](https://api.browser-use.com/api/v2/tasks) <br>
- [Browser Use API Credits Endpoint](https://api.browser-use.com/api/v2/credits) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BROWSER_USE_API_KEY and sends task descriptions to Browser Use's cloud API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
