## Description: <br>
Zoom Admin provides a managed OAuth integration for administering Zoom users, meetings, webinars, recordings, and account settings with admin-level access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operations administrators use this skill to administer an explicitly authorized Zoom workspace through Maton's managed OAuth gateway. It supports listing and managing users, meetings, webinars, recordings, connections, and account settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent could administer the wrong Zoom account if multiple OAuth connections are active. <br>
Mitigation: Specify the intended Maton connection when multiple accounts exist and confirm the account before making requests. <br>
Risk: Admin-level create, update, or delete actions can change users, meetings, webinars, recordings, or account settings. <br>
Mitigation: Review each write action, including the target resource and intended effect, before approval. <br>
Risk: An authorized connection may retain access longer than needed. <br>
Mitigation: Revoke the Maton Zoom connection when the administrative task is complete or access is no longer needed. <br>


## Reference(s): <br>
- [Zoom Admin skill page](https://clawhub.ai/byungkyu/skills/zoom-admin-api) <br>
- [Maton homepage](https://maton.ai) <br>
- [API Gateway skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline HTTP paths and Python, JavaScript, or shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY, network access, and an explicitly authorized Zoom Admin OAuth connection.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
