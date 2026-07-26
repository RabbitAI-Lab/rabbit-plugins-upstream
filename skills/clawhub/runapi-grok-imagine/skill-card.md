## Description: <br>
Generate and edit images and videos with Grok Imagine through RunAPI, using the CLI for one-off tasks and SDKs for application integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create, edit, animate, upscale, or transform media through RunAPI's Grok Imagine model. It guides one-off CLI usage and SDK-based application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunAPI and Grok Imagine are external paid or metered services. <br>
Mitigation: Confirm the user is comfortable using the external service and any associated account, billing, pricing, and rate-limit terms before running generation tasks. <br>
Risk: Authentication may use a local RunAPI API key or saved CLI login. <br>
Mitigation: Prefer environment-based authentication or saved CLI config, avoid exposing tokens in commands or logs, and use browser login only when the user explicitly wants interactive authentication. <br>
Risk: RunAPI-generated file URLs are temporary. <br>
Mitigation: Download and store generated images or videos in durable storage within 7 days when the user needs long-term access. <br>
Risk: Using the CLI as a production integration layer can create brittle application behavior. <br>
Mitigation: Use the target-language SDK path for app, backend, worker, webhook, or production integrations. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/runapi-ai/skills/runapi-grok-imagine) <br>
- [RunAPI Grok Imagine homepage](https://runapi.ai/models/grok-imagine) <br>
- [RunAPI Grok Imagine model documentation](https://runapi.ai/models/grok-imagine.md) <br>
- [RunAPI xAI provider documentation](https://runapi.ai/providers/xai.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>
- [Grok Imagine video 1.5 fast](https://runapi.ai/models/grok-imagine/video-1.5-fast.md) <br>
- [Grok Imagine text to image](https://runapi.ai/models/grok-imagine/text-to-image.md) <br>
- [Grok Imagine edit image](https://runapi.ai/models/grok-imagine/edit-image.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and SDK package references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce RunAPI task IDs, API responses, and temporary generated media URLs when the agent executes the described CLI or SDK workflows.] <br>

## Skill Version(s): <br>
0.2.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
