## Description:

Generate FUZZ music from exact lyrics or instrumental briefs with Producer through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create music generation requests for RunAPI Producer, execute one-off tasks through the RunAPI CLI, or integrate Producer into applications through the SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or selected media inputs may be sent to RunAPI under the user's authentication.

Mitigation: Use only intended inputs, confirm the active RunAPI authentication before submission, and avoid sending sensitive media unless approved.

Risk: Producer executions may incur paid RunAPI tasks.

Mitigation: Validate the request before submission, submit once, and require user authorization before creating any replacement paid task.

Risk: Generated audio and result files may be saved in the workspace.

Mitigation: Review saved outputs before sharing or committing them and remove artifacts that should not persist.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/runapi-ai/skills/runapi-producer)
- [RunAPI Producer homepage](https://runapi.ai/models/producer)
- [RunAPI Producer model overview](https://runapi.ai/models/producer.md)
- [RunAPI Producer provider overview](https://runapi.ai/providers/producer.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Producer SDK](https://github.com/runapi-ai/producer-sdk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with shell command examples and JSON request, task, and result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated audio and complete non-media results in the workspace after RunAPI execution.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
