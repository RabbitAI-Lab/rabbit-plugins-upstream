## Description: <br>
Uploads files from an agent workspace to a hosted bridge server and returns direct download or preview URLs for the owner. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrbeandev](https://clawhub.ai/user/mrbeandev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent needs to export generated files, share results, or provide preview and download links to its owner through a user-provided or temporary bridge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous mode can run external bridge server code and expose a temporary public tunnel. <br>
Mitigation: Use manual mode or a server you control when possible; review server code before autonomous mode, approve tunnel creation explicitly, and close temporary tunnels promptly. <br>
Risk: Uploaded files and bridge credentials may expose sensitive data if the wrong file, destination, or key handling is approved. <br>
Mitigation: Confirm each exact file and destination before upload, avoid sensitive data unless necessary, keep API keys out of URLs when possible, and delete or rotate temporary keys after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mrbeandev/skills/file-links-tool) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API examples and URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return raw download URLs, preview URLs, curl commands, Python request examples, and environment variable setup guidance.] <br>

## Skill Version(s): <br>
3.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
