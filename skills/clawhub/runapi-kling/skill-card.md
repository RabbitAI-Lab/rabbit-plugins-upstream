## Description: <br>
Generate and edit video with Kling through RunAPI, using the RunAPI CLI for one-off generation and SDKs for application or backend integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create, edit, transform, and test Kling video-generation workflows through RunAPI. It supports one-off CLI tasks and guides production integrations toward official RunAPI SDKs rather than shelling out from application code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and referenced media are sent to the RunAPI/Kling service, and optional RUNAPI_API_KEY or saved CLI login credentials may be used. <br>
Mitigation: Confirm the user is comfortable with RunAPI/Kling service use before execution and manage API keys or saved CLI login state carefully. <br>
Risk: Generated file URLs are temporary and may expire. <br>
Mitigation: Download and store generated videos or other outputs in durable storage within 7 days when they need to be retained. <br>
Risk: Using the CLI as a production runtime integration layer can create brittle application behavior. <br>
Mitigation: Use the language-specific RunAPI SDK integration path for app, backend, worker, or production workflow integrations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-kling) <br>
- [RunAPI Kling model page](https://runapi.ai/models/kling) <br>
- [RunAPI Kling documentation](https://runapi.ai/models/kling.md) <br>
- [RunAPI Kuaishou provider page](https://runapi.ai/providers/kuaishou.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with CLI commands, SDK package names, request-field notes, and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference temporary generated media URLs that should be downloaded to durable storage within 7 days.] <br>

## Skill Version(s): <br>
0.2.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
