## Description:

One-click pipeline that turns a single idea into a complete video-production plan: produces a plan template for the user to review/adjust, then expands it into canvas shapes and applies them via drawToCanvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video production teams use the skill to turn a creative idea into a reviewable story, character, scene, shot, and keyframe plan, then apply the workflow to a canvas for video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy services, and the CLI stores API credentials locally.

Mitigation: Use the service only if you trust dLazy with those inputs; review the proposed generation scope before confirming and manage or rotate the API key through your account.

Risk: The external CLI and canvas implementations have not been audited in full, and the documentation contains a CLI version inconsistency.

Mitigation: Check the installed CLI version and review the proposed workflow before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown requirement summaries and a structured video-generation workflow applied to a canvas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user reviews and confirms the plan before canvas application.]

## Skill Version(s):

1.3.40 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
