## Description: <br>
Install and use the RunAPI CLI as the universal execution layer for RunAPI models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to install, authenticate, inspect, and automate RunAPI CLI workflows from terminals, servers, and CI jobs. It supports running RunAPI model tasks, passing JSON requests, polling async jobs, managing local callback listeners, and handling temporary media file uploads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes a remote installer script piped directly into a shell, including for server and CI use. <br>
Mitigation: Prefer the documented Homebrew formula or use a download-and-verify workflow before executing installer content in automation. <br>
Risk: RunAPI authentication can persist in local configuration. <br>
Mitigation: Prefer environment credentials or stdin token import for headless use, keep config file permissions restricted, and avoid placing API keys directly in command arguments. <br>
Risk: Listener operations can expose Listen Signing Secrets. <br>
Mitigation: Keep listener secrets out of logs and project config, rotate exposed secrets for the selected key, update local verifiers, and restart affected listeners. <br>
Risk: Local files passed as model media inputs may be uploaded to RunAPI. <br>
Mitigation: Review file paths before submission and avoid sending sensitive local media unless the upload is intended. <br>


## Reference(s): <br>
- [RunAPI model and CLI catalog](https://runapi.ai/models.md) <br>
- [RunAPI models homepage](https://runapi.ai/models) <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-cli) <br>
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and TOML configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may reference RUNAPI_API_KEY, local RunAPI config, task JSON, callback key IDs, listener secrets, and temporary file URLs.] <br>

## Skill Version(s): <br>
0.2.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
