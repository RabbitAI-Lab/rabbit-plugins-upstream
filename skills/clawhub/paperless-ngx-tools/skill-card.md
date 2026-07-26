## Description: <br>
Manage documents in Paperless-ngx - search, upload, tag, and retrieve. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[madmantim](https://clawhub.ai/user/madmantim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent search, list, retrieve, upload, download, and create metadata in a Paperless-ngx document archive through its REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Paperless-ngx token can allow an agent to read documents, upload files, download documents, and create metadata in the archive. <br>
Mitigation: Use the least-privilege Paperless account available and install only when this level of access is acceptable. <br>
Risk: Remote Paperless-ngx connections can expose document and token data if sent over an insecure channel. <br>
Mitigation: Prefer HTTPS for remote Paperless-ngx instances. <br>
Risk: Download commands can write document files to the filesystem. <br>
Mitigation: Pass a safe --output path when downloading files. <br>
Risk: Advanced API operations documented for direct use include update, delete, and bulk-edit actions. <br>
Mitigation: Explicitly approve any update, delete, or bulk API operation before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/madmantim/skills/paperless-ngx-tools) <br>
- [Paperless-ngx project](https://github.com/paperless-ngx/paperless-ngx) <br>
- [Paperless-ngx API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require PAPERLESS_URL and PAPERLESS_TOKEN; downloads can write document files to a user-selected output path.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
