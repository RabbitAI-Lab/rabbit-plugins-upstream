## Description:

Selects a dLazy model to generate images, videos, or audio based on the user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy media-generation commands for images, videos, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be uploaded to the third-party dLazy cloud service, where generated media is hosted.

Mitigation: Use only content suitable for third-party processing and review uploads before running generation commands.

Risk: Login can persist an API key locally.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials if persistent storage is undesirable.

Risk: Broad generation triggers may select this skill for non-media requests.

Mitigation: Confirm that the user wants image, video, or audio generation before invoking it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI source listed in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and shell commands; CLI JSON responses contain hosted media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images, videos, and audio are accessible through dLazy-hosted URLs.]

## Skill Version(s):

1.3.24 (source: ClawHub release; bundled skill frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
