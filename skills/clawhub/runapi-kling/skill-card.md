## Description: <br>
Generate and edit video with Kling through RunAPI. Use when the user asks an agent to create, edit, or transform video with Kling. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to generate, edit, and transform Kling videos through RunAPI, choosing CLI guidance for one-off work and SDK guidance for application or backend integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunAPI calls can incur provider costs, rate limits, and network dependency. <br>
Mitigation: Install and use the skill only when RunAPI Kling generation is intended, and confirm pricing, limits, and user approval before running generation commands. <br>
Risk: API-key or CLI login handling can expose credentials if copied into logs or commands carelessly. <br>
Mitigation: Prefer RUNAPI_API_KEY or saved CLI configuration, avoid printing secrets, and use interactive browser login only when the user explicitly wants it. <br>
Risk: Private media URLs sent to Kling may be processed by RunAPI or upstream providers. <br>
Mitigation: Avoid sending private or sensitive media URLs unless the user is comfortable with RunAPI processing them. <br>
Risk: Generated file URLs are temporary. <br>
Mitigation: Download generated media and store it in user-controlled durable storage within 7 days. <br>
Risk: Using the CLI as a production integration layer can create brittle application behavior. <br>
Mitigation: Use the language SDK path for applications, backends, workers, libraries, and production workflows. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/runapi-ai/skills/runapi-kling) <br>
- [RunAPI Kling homepage](https://runapi.ai/models/kling) <br>
- [RunAPI Kling model documentation](https://runapi.ai/models/kling.md) <br>
- [RunAPI Kuaishou provider comparison](https://runapi.ai/providers/kuaishou.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, request JSON guidance, and SDK integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides agents that may call RunAPI; generated media URLs are temporary and should be moved to durable storage within 7 days.] <br>

## Skill Version(s): <br>
0.2.14 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
