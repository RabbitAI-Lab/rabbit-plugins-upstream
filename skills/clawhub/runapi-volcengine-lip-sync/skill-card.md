## Description: <br>
Generate lip-sync video with Volcengine Lip Sync through RunAPI. Use when the user asks an agent to sync mouth movement in a source video to an audio track. Default to the RunAPI CLI for one-off generation; use SDKs only when integrating RunAPI into an app or backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create audio-driven lip-sync videos through RunAPI, using the CLI for one-off generation and SDK packages for application or backend integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence reports a clean verdict but low confidence because the scanner data did not include direct artifact inspection. <br>
Mitigation: Review the skill file and requested `runapi` binary and `RUNAPI_API_KEY` usage before installing in sensitive environments. <br>
Risk: Interactive browser login can block headless or automated agent runs. <br>
Mitigation: Prefer `RUNAPI_API_KEY` or saved CLI configuration, and use browser login only when the user explicitly requests an interactive flow. <br>
Risk: RunAPI-generated file URLs are temporary and may expire before downstream workflows finish. <br>
Mitigation: Download generated video outputs and store them in durable user-controlled storage within 7 days. <br>
Risk: Using the CLI as a production integration layer can make backend behavior brittle. <br>
Mitigation: Use the language-specific RunAPI SDK for application, backend, worker, webhook, or production workflow integrations. <br>


## Reference(s): <br>
- [Volcengine Lip Sync model documentation](https://runapi.ai/models/volcengine-lip-sync.md) <br>
- [Volcengine Lip Sync model homepage](https://runapi.ai/models/volcengine-lip-sync) <br>
- [ByteDance provider comparison](https://runapi.ai/providers/bytedance.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI agent guidance](https://github.com/runapi-ai/cli-skill) <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-volcengine-lip-sync) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, JSON] <br>
**Output Format:** [Markdown with shell commands, package names, and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to submit RunAPI tasks synchronously or asynchronously and to download temporary generated file URLs within 7 days.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
