## Description:

Helps users turn an idea into a confirmed video-production plan covering story, characters, scenes, frames, clips, and assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan a video from an idea, review its scenes and shots, and optionally create canvas workflows or generate media through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas planning and direct terminal generation instructions may lead to an unexpected execution path.

Mitigation: Review the proposed plan and commands, and confirm which workflow should run before execution.

Risk: Prompts and selected local media may be sent to dLazy's cloud services.

Mitigation: Share only material approved for external processing and review selected media before upload.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source (linked by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with plan summaries, inline shell commands, and media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before expanding plans or generating media.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
