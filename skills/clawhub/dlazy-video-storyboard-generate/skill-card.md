## Description:

Builds a video-generation pipeline from storyboard scenes and adds it to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn storyboard dialogue and scene prompts into an audio-and-video generation pipeline on a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the dLazy CLI requires command execution and installing or invoking a third-party package.

Mitigation: Review the CLI and prefer on-demand npx invocation if a persistent global installation is unnecessary.

Risk: Prompts and selected local media may be sent to dLazy cloud services.

Mitigation: Send only content you are authorized to share with dLazy.

Risk: Authentication may save an API key in local configuration.

Mitigation: Use an environment-variable API key if you do not want persistent credential storage.

Risk: The skill can change the canvas with generated storyboard elements.

Mitigation: Review proposed canvas changes before accepting them.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON configuration, Guidance]

**Output Format:** [JSON canvas pipeline with accompanying Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canvas elements include shared scene imagery and source audio, plus generated audio and video per storyboard.]

## Skill Version(s):

1.2.26 (source: ClawHub release; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
