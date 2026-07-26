## Description: <br>
Generate and transform music, audio, lyrics, and custom voice workflows with Suno through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create or transform music and audio, compose or blend lyrics, and prepare Suno custom voice workflows through RunAPI. It guides one-off CLI generation and SDK-based application integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Music prompts, lyrics, audio, or voice samples may be sent to RunAPI or Suno and may involve provider account costs. <br>
Mitigation: Confirm the user is comfortable with the provider transfer and expected costs before installing or using the skill, and avoid submitting sensitive content unless approved. <br>
Risk: Interactive browser login is not suitable for every agent or headless environment. <br>
Mitigation: Prefer environment-based API keys or saved CLI configuration for agent and headless use; use browser login only when interactive authentication is explicitly intended. <br>
Risk: RunAPI-generated file URLs are temporary and should not be treated as durable storage. <br>
Mitigation: Download and store generated audio, image, video, or related files in durable storage within the documented seven-day window. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-suno) <br>
- [RunAPI Suno model page](https://runapi.ai/models/suno) <br>
- [RunAPI Suno model documentation](https://runapi.ai/models/suno.md) <br>
- [RunAPI Suno provider comparison](https://runapi.ai/providers/suno.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the runapi CLI for one-off tasks, supports SDK guidance for application integrations, and may use the optional RUNAPI_API_KEY environment variable.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
