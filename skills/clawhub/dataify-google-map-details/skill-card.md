## Description: <br>
Submits Dataify Builder jobs that collect Google Maps details by URL, CID, location, or place ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit Dataify Google Maps detail collection jobs, then receive the resulting task ID, status, and dashboard location. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can invoke a third-party Dataify workflow and may reuse a saved DATAIFY_API_TOKEN. <br>
Mitigation: Confirm the intended token source and review the exact URL, CID, location, or place ID parameters before submission. <br>
Risk: Submitted jobs go to Dataify and may affect the user's Dataify account or usage quota. <br>
Mitigation: Use the skill only when creating Dataify Google Maps collection tasks is expected, and check the Dataify dashboard after submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-map-details) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>
- [Google Country Options](references/google_countries.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with optional shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful submissions report mode, spider_id, task_id, status, parameters, file_name, dashboard_url, and a short message.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
