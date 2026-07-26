## Description: <br>
Cache and reuse code from prior AI agent executions via Raysurfer. Search before coding, upload after success. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryx2](https://clawhub.ai/user/ryx2) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and coding agents use this skill to search Raysurfer for reusable cached code before implementing a task, then upload successful code for future reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send task descriptions, workflow metadata, and selected source files to a third-party Raysurfer service. <br>
Mitigation: Use only on code and tasks approved for third-party sharing, and manually inspect any file contents before upload. <br>
Risk: Cached or public snippets may be untrusted or unsuitable for the current project. <br>
Mitigation: Review, adapt, and test retrieved code before writing it into a project or running it. <br>
Risk: The security verdict flags the release as suspicious because remote code retrieval and upload behavior may not provide enough user control. <br>
Mitigation: Require explicit user consent for cache use, avoid private or regulated repositories, and skip Raysurfer operations when the API key is absent or the API is unreachable. <br>


## Reference(s): <br>
- [Raysurfer API Reference](artifact/references/api-reference.md) <br>
- [Raysurfer API](https://api.raysurfer.com) <br>
- [Raysurfer API Keys Dashboard](https://raysurfer.com/dashboard/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, code snippets, and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires RAYSURFER_API_KEY; search and upload operations communicate with Raysurfer APIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
