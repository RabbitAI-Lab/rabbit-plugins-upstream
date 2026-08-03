## Description: <br>
A project memory skill that tracks status, milestones, owners, and blockers so agents managing ongoing work can maintain a live picture of every project. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to help agents store, recall, update, and close project records that include goals, owners, milestones, blockers, decisions, and outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project status, owners, milestones, and blockers are sent to an external BlueColumn/Supabase service. <br>
Mitigation: Install only when that data sharing is approved, and avoid sending secrets, regulated data, sensitive HR details, or confidential blocker information. <br>
Risk: Broad recall queries may expose more project context than a user needs for a specific status check. <br>
Mitigation: Prefer narrower recall queries when full project visibility is not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-projects) <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends project-management details to BlueColumn's external service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
