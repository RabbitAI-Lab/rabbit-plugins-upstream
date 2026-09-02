## Description:

Converts storyboard context into a video-generation canvas pipeline with shared scene and audio inputs plus per-shot cloned audio and video nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to turn storyboard entries into a structured canvas pipeline for audio cloning and video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the dLazy CLI/API and may send prompts and uploaded media to dLazy cloud endpoints.

Mitigation: Use it only when SaaS processing by dLazy is expected and the user has permission to send storyboard media to those endpoints.

Risk: The skill stores or uses a dLazy API key through local CLI configuration or DLAZY_API_KEY.

Mitigation: Use appropriate account controls and rotate or revoke the key when the workflow no longer needs access.

Risk: Clawscan marked the release suspicious because the terminal-based image-generation workflow is broader than storyboard canvas setup.

Mitigation: Review generated pipelines and dLazy commands before execution, and keep use scoped to the expected storyboard-to-canvas task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON pipeline examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a canvas pipeline from storyboard entries, aspect ratio, resolution, dialogue text, and video prompts.]

## Skill Version(s):

1.2.9 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
