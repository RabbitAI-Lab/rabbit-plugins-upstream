## Description: <br>
Microsoft OneDrive helps agents manage OneDrive files, folders, drives, and sharing through Maton-managed OAuth over Microsoft Graph. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to list, upload, download, organize, or share files in a connected OneDrive account through Maton commands or API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, move, share, and delete files or folders in a connected OneDrive account. <br>
Mitigation: Confirm the target resource and intended effect before write, share, or delete operations, as required by the artifact. <br>
Risk: Requests require MATON_API_KEY and a Maton-managed OAuth connection to OneDrive. <br>
Mitigation: Protect the API key, use the intended connection explicitly when multiple connections exist, and revoke unused connections. <br>
Risk: Downloaded file links may be pre-authenticated and valid for a short time. <br>
Mitigation: Avoid exposing download URLs in logs or public outputs and handle retrieved file content according to the user's data handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/one-drive) <br>
- [Maton OneDrive API base](https://api.maton.ai/one-drive/v1.0/{resource}) <br>
- [Maton](https://maton.ai) <br>
- [Maton API Gateway skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with CLI, HTTP, Python, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a Maton-managed OneDrive OAuth connection.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
