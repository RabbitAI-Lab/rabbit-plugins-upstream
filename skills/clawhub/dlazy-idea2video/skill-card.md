## Description:

Turns a video idea into a reviewable production plan and canvas workflow for generating scenes, shots, and a final video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn an idea into a video-production plan, review it, and build a canvas workflow for generating and combining video segments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mixes a canvas-only plan with instructions to execute terminal commands, making user control less clear.

Mitigation: Confirm the intended workflow with the user and review each proposed command before execution.

Risk: The dLazy CLI stores an API key locally and sends prompts or selected media files to dLazy cloud services.

Mitigation: Review the data selected for upload and protect or revoke the API key as needed.

Risk: Installing or running the dLazy CLI allows third-party code to run locally.

Mitigation: Review the CLI package and installation command before using a global install or npx.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Canvas workflow configuration, Shell commands, Media links]

**Output Format:** [Markdown plan followed by structured canvas shapes; generated media links when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before applying the plan; video generation uses dLazy services.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
