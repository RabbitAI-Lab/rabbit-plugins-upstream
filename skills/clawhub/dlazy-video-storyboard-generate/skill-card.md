## Description:

Converts storyboard context into a canvas-ready video generation pipeline with audio, image, and per-scene video elements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to turn storyboard entries, aspect ratio, and resolution into a JSON pipeline that can be drawn onto a canvas for video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI/API integration that can send prompts and media files to dLazy services and store or use a dLazy API key.

Mitigation: Install only when this third-party service and data flow are expected; use a dedicated, rotatable API key and review prompts and media before submission.

Risk: Security evidence marks the release suspicious because the stated storyboard pipeline purpose and runtime image-generation instructions are inconsistent.

Mitigation: Review the skill before installation and consider narrowing or splitting storyboard pipeline generation from terminal image generation.

Risk: The skill can add generated pipeline elements to a canvas.

Mitigation: Confirm the generated pipeline structure and target canvas changes before allowing the agent to draw them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with JSON pipeline snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces canvas pipeline elements sized from storyboard aspect ratio and resolution; uses dLazy CLI/API when terminal generation is invoked.]

## Skill Version(s):

1.2.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
