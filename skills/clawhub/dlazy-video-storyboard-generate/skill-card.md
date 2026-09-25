## Description:

Converts storyboard details into a video-generation pipeline that can be drawn onto a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to turn storyboard context into a video-generation pipeline with shared scene and audio inputs plus per-shot cloned-audio and video steps that can be added to a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires dLazy CLI access and may store an API key in local CLI configuration.

Mitigation: Install only from the expected dLazy package or source, use a rotatable API key, restrict local config access, and revoke the key when it is no longer needed.

Risk: Prompts and referenced media files may be sent to dLazy cloud endpoints.

Mitigation: Avoid submitting confidential, regulated, or rights-restricted media unless the user has approved that cloud processing path.

Risk: The workflow may mutate a canvas and uses terminal-driven generation broader than the storyboard task.

Mitigation: Review the generated pipeline before applying it to a canvas and run generation commands one at a time in a controlled environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON pipeline examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas pipeline elements and generated media URLs through the dLazy workflow.]

## Skill Version(s):

1.2.18 (source: release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
