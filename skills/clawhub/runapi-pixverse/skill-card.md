## Description: <br>
Create, edit, transition, and extend PixVerse V6 videos through RunAPI. Use when the user asks an agent to create video from text, images, references, transitions, or a completed PixVerse task. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate, edit, transition, and extend PixVerse V6 videos through RunAPI. It guides one-off CLI use and SDK integration paths for application or backend workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunAPI CLI or SDK use may require a RunAPI API key. <br>
Mitigation: Use environment authentication or saved CLI configuration, avoid exposing the key in logs, and use browser login only for explicitly interactive sessions. <br>
Risk: Generated video URLs are temporary. <br>
Mitigation: Download and store generated videos in durable storage within 7 days when long-term retention is needed. <br>
Risk: PixVerse continuation workflows can fail or target the wrong source if a caller-owned video URL is substituted for a RunAPI task. <br>
Mitigation: Use an account-owned completed RunAPI source_task_id for extend-video workflows. <br>


## Reference(s): <br>
- [RunAPI PixVerse homepage](https://runapi.ai/models/pixverse) <br>
- [RunAPI PixVerse model overview](https://runapi.ai/models/pixverse.md) <br>
- [PixVerse V6 model details](https://runapi.ai/models/pixverse/pixverse-v6.md) <br>
- [RunAPI PixVerse provider comparison](https://runapi.ai/providers/pixverse.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell commands and request JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated video URLs are temporary and should be downloaded or stored in durable storage within 7 days.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
