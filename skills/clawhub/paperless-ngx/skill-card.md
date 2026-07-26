## Description: <br>
Interact with Paperless-ngx document management system via REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oskarstark](https://clawhub.ai/user/oskarstark) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to help an agent manage a Paperless-ngx instance, including searching documents, uploading and downloading files, and organizing metadata such as tags, correspondents, and document types. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A privileged Paperless-ngx API token can allow access to and changes in sensitive documents. <br>
Mitigation: Use a dedicated least-privilege API token and install the skill only for a Paperless-ngx instance the agent is intended to manage. <br>
Risk: Incorrect URL or broad document actions can affect the wrong Paperless-ngx instance or many documents at once. <br>
Mitigation: Verify PAPERLESS_URL before use and require explicit confirmation before delete, bulk edit, reprocess, or broad metadata update operations. <br>
Risk: Downloaded files may expose local copies of sensitive documents. <br>
Mitigation: Avoid unnecessary local downloads and handle downloaded files according to the user's document retention and access controls. <br>


## Reference(s): <br>
- [ClawHub Paperless-ngx skill page](https://clawhub.ai/oskarstark/skills/paperless-ngx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with REST API curl examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PAPERLESS_URL and PAPERLESS_TOKEN; actions may access, download, upload, update, or delete sensitive documents depending on token permissions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
