## Description:

Selects a dLazy video model for text-to-video, image-to-video, frame-guided video, digital human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run a dLazy video model for generating or editing short videos from prompts, images, audio, or existing video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be uploaded to the third-party dLazy service.

Mitigation: Use only media and prompts approved for third-party processing; avoid private or regulated content without appropriate authorization.

Risk: A dLazy API key is stored in local CLI configuration and may be exposed if the configuration is disclosed.

Mitigation: Protect the local configuration and rotate or revoke the key in the dLazy dashboard if it is exposed.

Risk: Installing and running the third-party CLI executes package code.

Mitigation: Install only if you trust dLazy and the @dlazy/cli package; use the pinned npx invocation to avoid a persistent global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI link in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and generated-video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses include JSON containing hosted output URLs.]

## Skill Version(s):

1.4.25 (source: ClawHub release metadata; bundled frontmatter lists 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
