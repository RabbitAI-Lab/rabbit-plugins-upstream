## Description:

Helps turn an idea into a reviewable video-production plan with story, character, scene, shot, image, and video stages, then prepares a canvas workflow for execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn a video idea into a staged production plan, review the plan, and prepare a canvas workflow for generating visual assets and assembling a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI handles prompts, selected media, generated outputs, and a locally stored API key.

Mitigation: Install only if you trust the service, avoid submitting sensitive media or prompts, and protect or rotate the API key as needed.

Risk: The skill instructs the agent to execute terminal commands, which could affect unexpected local files if a command is unsafe.

Mitigation: Review each proposed command and its file paths and shell metacharacters before approving execution; prefer on-demand CLI use or review the CLI before global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI package linked by the skill](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown plan summaries, structured canvas shapes, and optional CLI commands and media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The plan requires user confirmation before canvas expansion; generated media depends on external services.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
