## Description: <br>
Enrich, search, and manage company and professional data, lists, saved searches, and signals using the Specter intelligence platform via CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[froemic](https://clawhub.ai/user/froemic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and business-development operators use this skill to install and operate the Specter CLI for company enrichment, professional lookup, list management, saved-search review, talent signals, investor-interest signals, and entity extraction from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Specter API key for authenticated API access. <br>
Mitigation: Use trusted Specter credentials, prefer least-privileged credentials if Specter supports them, and avoid exposing the key in prompts, logs, or shared outputs. <br>
Risk: The skill documents live delete operations for saved searches and company or people lists. <br>
Mitigation: Require explicit human approval before deletion commands, verify resource IDs, and confirm whether recovery is possible before execution. <br>
Risk: The skill can retrieve and enrich business and professional contact data and may consume team credits. <br>
Mitigation: Confirm the intended scope before enrichment or search commands, review outputs before sharing, and avoid unnecessary bulk requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/froemic/skills/specter) <br>
- [Publisher profile](https://clawhub.ai/user/froemic) <br>
- [Specter API Console](https://app.tryspecter.com/settings/api-console) <br>
- [Specter API base URL](https://app.tryspecter.com/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, configuration notes, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that call the Specter API and manage live Specter resources.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
