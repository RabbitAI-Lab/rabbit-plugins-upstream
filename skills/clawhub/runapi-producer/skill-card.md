## Description: <br>
Generate FUZZ music from exact lyrics or instrumental briefs with Producer through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate music with Producer FUZZ models through RunAPI, either from exact lyrics plus style guidance or from instrumental prompts. It guides one-off CLI use and SDK-based application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts or lyrics may be sent to RunAPI when using the CLI or SDKs. <br>
Mitigation: Avoid submitting lyrics, prompts, or briefs that should not be processed by RunAPI, and use approved authentication handling for RUNAPI_API_KEY or saved CLI login. <br>
Risk: Generated media URLs are temporary. <br>
Mitigation: Download generated audio and related assets and store them in durable storage when they need to be retained. <br>
Risk: Using the CLI as a production runtime integration layer can make applications brittle. <br>
Mitigation: Use the appropriate RunAPI SDK for applications, workers, services, and other production integrations. <br>


## Reference(s): <br>
- [Producer model overview](https://runapi.ai/models/producer.md) <br>
- [Producer model details and pricing](https://runapi.ai/models/producer/fuzz-2.0.md) <br>
- [Producer provider page](https://runapi.ai/providers/producer.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI Producer homepage](https://runapi.ai/models/producer) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, SDK package names, request guidance, and result-handling notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference RunAPI CLI authentication, SDK integration paths, asynchronous task polling, and temporary generated media URLs.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
