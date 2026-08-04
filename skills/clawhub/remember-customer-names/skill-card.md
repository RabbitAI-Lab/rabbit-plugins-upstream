## Description: <br>
This skill helps agents remember customer names, roles, companies, and relevant conversation details for more personalized customer interactions using the BlueColumn API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer-facing agents and their operators use this skill to store, recall, and update customer identity cards so conversations can use accurate names, roles, company context, and relevant business details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer names, roles, companies, and personal notes may be sent to and retained by a third-party service. <br>
Mitigation: Use only with approved business context, collect consent where required, and avoid unnecessary family, health, financial, or unrelated personal details. <br>
Risk: Stored customer profile notes may become inaccurate or lack clear correction and deletion controls. <br>
Mitigation: Define a review, correction, and deletion process before using the skill in customer-facing workflows. <br>
Risk: The skill requires a live BlueColumn API key for write and recall operations. <br>
Mitigation: Store BLUECOLUMN_API_KEY in an approved secret manager, restrict access to authorized agents, and rotate it if exposed. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-customer-names) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with bash and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY; stores and retrieves customer identity-card text through BlueColumn/Supabase APIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
