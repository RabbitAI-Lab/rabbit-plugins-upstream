## Description:

Generates detailed short-video storyboard scripts from user-provided themes, copy, or outlines while preserving the original wording in each shot's spoken script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and storytellers use the skill to turn themes, structured copy, and outlines into shot-by-shot short-video scripts with visual direction and production notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The storyboard-only scope conflicts with instructions that require cloud image generation.

Mitigation: For text-only storyboard work, use the storyboard workflow without image-generation commands; require explicit approval before expanding the task to image generation.

Risk: Image-generation use may send prompts or supplied media to dLazy services and uses credentials stored in the disclosed CLI configuration.

Mitigation: Before image generation, approve that scope, review which prompts and files will be sent, check service costs, and review credential storage.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown storyboard with global video parameters and numbered shots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scene, camera, and production notes; spoken script is allocated from the user's original copy.]

## Skill Version(s):

1.2.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
