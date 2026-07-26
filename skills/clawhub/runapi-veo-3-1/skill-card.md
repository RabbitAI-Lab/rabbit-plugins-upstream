## Description: <br>
Generate and edit video with Veo 3 through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create, edit, extend, and upscale Veo 3 videos through RunAPI. It supports one-off CLI generation and SDK-based application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use a RunAPI API key or saved CLI authentication to send generation requests to an external provider. <br>
Mitigation: Use environment-based or saved CLI authentication, avoid exposing secrets in prompts or logs, and confirm external-provider use is acceptable for the task. <br>
Risk: RunAPI-generated file URLs are temporary and may expire before assets are retained. <br>
Mitigation: Download generated videos or related assets into durable storage within the documented temporary URL window. <br>
Risk: Using the CLI as a production runtime integration layer can make app integrations harder to operate and test. <br>
Mitigation: Use the RunAPI SDK path for application, backend, worker, library, webhook, or production workflow integrations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-veo-3-1) <br>
- [RunAPI Veo 3.1 homepage](https://runapi.ai/models/veo-3.1) <br>
- [RunAPI Veo 3.1 model documentation](https://runapi.ai/models/veo-3.1.md) <br>
- [RunAPI Google provider comparison](https://runapi.ai/providers/google.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands, SDK package names, and JSON request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents toward RunAPI CLI use for one-off video tasks and SDK use for application integrations.] <br>

## Skill Version(s): <br>
0.2.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
