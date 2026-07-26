## Description: <br>
Generate and edit images with Qwen Image through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate, remix, or edit images with Qwen Image through RunAPI, choosing CLI commands for one-off tasks and SDK guidance for application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or edited image requests go through RunAPI and may involve provider billing, rate limits, authentication, and temporary output URLs. <br>
Mitigation: Use an API key or saved CLI authentication only when appropriate for the workspace, check RunAPI pricing and limits, and persist needed outputs outside temporary URLs. <br>
Risk: Using the CLI as an application runtime integration path can create brittle production workflows. <br>
Mitigation: Use the documented SDK integration path for application, backend, worker, library, webhook, or production codebase integrations. <br>


## Reference(s): <br>
- [RunAPI Qwen Image model page](https://runapi.ai/models/qwen-image) <br>
- [RunAPI Qwen Image documentation](https://runapi.ai/models/qwen-image.md) <br>
- [RunAPI Alibaba provider page](https://runapi.ai/providers/alibaba.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with shell command and SDK package examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include RunAPI CLI or SDK instructions, authentication guidance, and generated image handling guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
