## Description: <br>
Triggers when a user provides a pet toy area video URL or file for analysis; supports local video uploads or network URLs to call server-side APIs for toy interaction behavior recognition, tracking interaction frequency, duration, and toy preference per pet, generating daily activity curves and trend comparisons to detect declining activity that may indicate illness or depression. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze pet toy-area videos or URLs for toy interaction behavior, interaction frequency and duration, toy preference, daily activity trends, and historical report lookup. Results are behavior references and should not be treated as disease or emotional diagnoses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet-area videos or URLs are sent to the Life Emergence cloud service for analysis. <br>
Mitigation: Use only media appropriate for that service and avoid sensitive private footage unless the deployment policy allows it. <br>
Risk: The skill can create or reuse a local account identity and store authentication tokens and report history data in the workspace. <br>
Mitigation: Deploy in a controlled workspace, protect local storage, and remove or rotate stored credentials when decommissioning the skill. <br>
Risk: Cloud history report queries can return prior analysis records associated with the local identity. <br>
Mitigation: Limit access to workspaces where report history should be visible and review history outputs before sharing them. <br>


## Reference(s): <br>
- [Pet toy interaction API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-toy-interaction-activity-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text reports, with optional JSON-oriented detail and saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return structured analysis results, report links, and Markdown tables for cloud history reports.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
