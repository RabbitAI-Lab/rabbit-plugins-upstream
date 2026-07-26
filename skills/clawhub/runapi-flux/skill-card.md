## Description: <br>
Generate and remix images with Flux through RunAPI. Use when the user asks an agent to create or transform images with Flux. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agents use this skill to create or transform images with Flux through RunAPI. It guides one-off CLI generation and SDK-based application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, source images, and generated outputs are sent to RunAPI as an external image generation service. <br>
Mitigation: Use the skill only with data appropriate for RunAPI processing and follow the user's or organization's data-sharing policy. <br>
Risk: Agents may need RunAPI account access through an API key, saved CLI auth, or interactive login. <br>
Mitigation: Prefer RUNAPI_API_KEY or saved CLI configuration for the intended account, and use browser login only when the user explicitly requests interactive authentication. <br>
Risk: Generated media URLs returned by RunAPI are temporary. <br>
Mitigation: Download generated files and store them in durable storage within 7 days. <br>


## Reference(s): <br>
- [RunAPI Flux model documentation](https://runapi.ai/models/flux.md) <br>
- [RunAPI Flux homepage](https://runapi.ai/models/flux) <br>
- [Black Forest Labs provider comparison](https://runapi.ai/providers/black-forest-labs.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands and SDK package names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference temporary generated file URLs that should be downloaded to durable storage within 7 days.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
