## Description: <br>
Pipedrive API helps agents use Maton-hosted Pipedrive endpoints with managed OAuth to work with deals, persons, organizations, activities, and related CRM records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators can use this skill to configure agent-assisted Pipedrive CRM API workflows, including querying or managing deals, people, organizations, and activities. It is intended for productivity and workflow automation, not tasks that require independent human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends CRM data through the documented remote endpoint under the user's API key. <br>
Mitigation: Install only for intended Maton and Pipedrive API use, use task-specific access, and avoid sending sensitive CRM data unless the workflow has been reviewed. <br>
Risk: The security review reports broad shell and file authority plus generic or contradictory documentation. <br>
Mitigation: Review commands and file actions before execution, grant only the access needed for the task, and avoid using the skill for generic automation. <br>
Risk: API credentials can be exposed if copied into source files, logs, or prompts. <br>
Mitigation: Store MATON_API_KEY in the environment, do not commit credentials, and rotate the key if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pipedrive-api) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Maton Pipedrive deals endpoint example](https://api.maton.ai/pipedrive/api/v1/deals) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell and Python examples; API responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and network access to the documented Maton-hosted Pipedrive API endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
