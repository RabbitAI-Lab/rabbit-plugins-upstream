## Description:

Converts storyboard context into a video-generation pipeline and adds the resulting audio, image, and video elements to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn storyboard entries, dialogue, aspect ratio, and resolution into a structured canvas pipeline for cloned audio, scene images, and generated video clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mixes storyboard canvas generation with a separate command-driven dLazy image-generation workflow.

Mitigation: Review the workflow before installation and split or remove unrelated image-generation command behavior before broad use.

Risk: Use of the dLazy CLI can store or read an API key and send prompts or selected media files to dLazy services.

Mitigation: Install only in environments where dLazy CLI authentication, cloud processing, and media upload are acceptable.

Risk: The skill can modify the user's canvas by adding generated pipeline elements.

Mitigation: Review the proposed canvas pipeline before applying it to production or shared workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with JSON pipeline examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces canvas pipeline instructions and may call the dLazy CLI when the agent follows the skill workflow.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
