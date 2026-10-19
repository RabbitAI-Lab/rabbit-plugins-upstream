## Description:

Turns articles and other documents into narrated explainer videos through a hosted outline, storyboard, voiceover, and production workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to turn articles, text, or uploaded documents into narrated explainer, training, or report videos with dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to the dLazy service; uploads may include sensitive documents.

Mitigation: Review service terms and intended upload scope before use; avoid attaching sensitive documents without approval.

Risk: The skill installs a third-party CLI and authentication can persist an API key locally.

Mitigation: Review the pinned CLI before installing, protect or rotate credentials, and use DLAZY_API_KEY per invocation when persistent storage is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with command examples and project responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service may return video results through project conversations.]

## Skill Version(s):

1.0.34 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
