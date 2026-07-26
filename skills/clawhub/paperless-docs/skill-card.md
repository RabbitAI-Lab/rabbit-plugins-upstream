## Description: <br>
Manage documents in Paperless-ngx - search, upload, tag, and retrieve. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[madmantim](https://clawhub.ai/user/madmantim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent search, list, upload, download, and organize documents in a configured Paperless-ngx instance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured Paperless token gives the agent the same document and metadata access allowed by that token. <br>
Mitigation: Use a limited Paperless account or token where possible, and review commands before allowing reads, uploads, metadata creation, or downloads. <br>
Risk: Download operations can write document files to local paths chosen at runtime. <br>
Mitigation: Confirm download destinations before execution and avoid writing sensitive documents to shared or unintended directories. <br>
Risk: Advanced direct API operations can modify, bulk edit, or delete Paperless records. <br>
Mitigation: Review the API method, document IDs, and payload before running advanced operations beyond the convenience scripts. <br>


## Reference(s): <br>
- [Paperless-ngx API Reference](references/api.md) <br>
- [Paperless-ngx Project](https://github.com/paperless-ngx/paperless-ngx) <br>
- [ClawHub Skill Page](https://clawhub.ai/madmantim/skills/paperless-docs) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON from helper scripts, with Markdown guidance and shell commands from the agent.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PAPERLESS_URL and PAPERLESS_TOKEN; download operations may write files to the requested output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
