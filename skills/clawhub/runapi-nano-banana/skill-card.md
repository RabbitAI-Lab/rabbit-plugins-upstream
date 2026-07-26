## Description: <br>
Generate and edit images with Nano Banana through RunAPI, using the CLI for one-off tasks and SDKs for application or backend integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate or edit Nano Banana images through RunAPI. It guides one-off CLI usage and SDK-based application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may call RunAPI over the network and use a RunAPI API key or saved CLI login. <br>
Mitigation: Install it only when RunAPI-backed Nano Banana generation or editing is intended, and keep RUNAPI_API_KEY scoped to RunAPI. <br>
Risk: RunAPI-generated file URLs are temporary and should not be treated as long-term assets. <br>
Mitigation: Download generated images or other returned files into durable storage within the documented seven-day window. <br>
Risk: Using the CLI as a production integration layer can create brittle application behavior. <br>
Mitigation: Use the documented language SDK path for app, backend, worker, service, webhook, or other production workflow integration. <br>


## Reference(s): <br>
- [Nano Banana model documentation](https://runapi.ai/models/nano-banana.md) <br>
- [RunAPI Google provider page](https://runapi.ai/providers/google.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI Nano Banana homepage](https://runapi.ai/models/nano-banana) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>
- [Publisher profile](https://clawhub.ai/user/runapi-ai) <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-nano-banana) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and SDK package names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide use of the runapi CLI, RunAPI SDKs, RUNAPI_API_KEY, and temporary generated file URLs.] <br>

## Skill Version(s): <br>
0.2.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
