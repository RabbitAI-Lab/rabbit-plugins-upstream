## Description:

Generate and edit images with Seedream through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, transform, and verify Seedream image outputs through RunAPI CLI workflows or SDK integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images, prompts, and request data may be sent to RunAPI for processing.

Mitigation: Use only content approved for RunAPI processing and review request data before submitting tasks.

Risk: RunAPI authentication can expose API key or saved CLI credentials if handled carelessly.

Mitigation: Prefer environment-based authentication or saved CLI configuration and avoid hardcoding credentials in request files or generated code.

Risk: Retries or replacement submissions can create additional paid tasks.

Mitigation: Submit once, wait on the existing task when possible, and request user authorization before any additional paid job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-seedream)
- [RunAPI Seedream model page](https://runapi.ai/models/seedream)
- [RunAPI Seedream documentation](https://runapi.ai/models/seedream.md)
- [ByteDance provider overview](https://runapi.ai/providers/bytedance.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Seedream SDK integration](https://github.com/runapi-ai/seedream-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request files, task/result JSON, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RunAPI CLI or SDK access and verification of generated image deliverables.]

## Skill Version(s):

0.2.11 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
