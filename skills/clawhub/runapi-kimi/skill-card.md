## Description: <br>
Call the Kimi API (kimi-k3, kimi-k2.7-code, kimi-k2.6, kimi-k2.5) through RunAPI using the official OpenAI SDK or compatible clients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure agents or applications for Kimi model access through RunAPI using OpenAI-compatible, Anthropic-compatible, or Gemini-compatible client surfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API credentials could be exposed if copied into source files, commits, or shell history. <br>
Mitigation: Store RunAPI credentials only in environment variables or a secret manager. <br>
Risk: Using the skill routes model requests through RunAPI. <br>
Mitigation: Confirm RunAPI is an approved provider for the intended Kimi access before installation or use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-kimi) <br>
- [RunAPI Kimi model documentation](https://runapi.ai/models/kimi.md) <br>
- [RunAPI Kimi homepage](https://runapi.ai/models/kimi) <br>
- [RunAPI Moonshot AI provider page](https://runapi.ai/providers/moonshot-ai.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with dotenv, Python, TypeScript, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires RunAPI API credentials in environment variables and routes model requests through RunAPI.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
