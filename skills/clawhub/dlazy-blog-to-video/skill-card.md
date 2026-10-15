## Description:

Helps turn blog posts and other documents into narrated videos with outlines, storyboards, voiceovers, and assembly through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to request narrated video versions of blog posts or other supplied documents for social, educational, or presentation use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The blog-to-video title understates the broader document and file-to-video workflow.

Mitigation: Review the requested workflow and supplied files before invoking the skill.

Risk: Prompts and attached local files are sent to dLazy services, and use requires a dLazy API key.

Mitigation: Use only if third-party processing is acceptable; avoid confidential files and manage the API key securely.

Risk: Using the skill installs or runs the pinned dLazy CLI.

Mitigation: Review the CLI and its requested access before installation or execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Streaming text responses with project guidance and potential video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through the dLazy service; output depends on the project and supplied material.]

## Skill Version(s):

1.0.28 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
