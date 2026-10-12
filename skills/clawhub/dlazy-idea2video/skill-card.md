## Description:

Helps creators turn an idea into a reviewed video-production plan covering story, characters, scenes, shots, and generated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan a video from an idea, review the proposed workflow, and generate or arrange the resulting visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions conflict between a canvas planning workflow and mandatory terminal execution.

Mitigation: Clarify the intended workflow with the user and obtain approval before running generation commands.

Risk: CLI installation and login can install software and store a dLazy API key locally.

Mitigation: Review the CLI package and request explicit approval before installation or login.

Risk: Prompts and referenced media may be sent to dLazy services.

Mitigation: Review data sensitivity and obtain approval before uploading files or generating media.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Markdown, Workflow configuration, Shell commands, Media URLs]

**Output Format:** [Markdown plan summaries, canvas workflow shapes, and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plan confirmation is requested before generation; media generation can use dLazy services.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release; bundled frontmatter says 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
