## Description:

Generate and edit video with Hailuo through RunAPI. Use when the user asks an agent to create, edit, or transform video with Hailuo. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, or transform video with Hailuo through RunAPI while selecting the correct CLI or SDK route for the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to RunAPI/Hailuo may be uploaded to the service.

Mitigation: Review generated requests before submission, especially when sensitive media or prompts are involved.

Risk: Submitting RunAPI tasks may incur costs.

Mitigation: Authenticate intentionally, submit each task once, preserve task evidence, and avoid replacement paid requests without user authorization.

Risk: Generated media deliverables may be missing, empty, or the wrong MIME type.

Mitigation: Download every requested deliverable and verify each file is non-empty and matches the expected video MIME family before reporting completion.

## Reference(s):

- [RunAPI Hailuo homepage](https://runapi.ai/models/hailuo)
- [Hailuo model documentation](https://runapi.ai/models/hailuo.md)
- [MiniMax provider documentation](https://runapi.ai/providers/minimax.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Hailuo SDK](https://github.com/runapi-ai/hailuo-sdk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to submit RunAPI tasks, preserve JSON responses, and verify downloaded video media.]

## Skill Version(s):

0.2.9 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
