## Description:

This skill guides agents to generate short-video spoken scripts with high contrast, strong resonance, story structure, and personal IP attributes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agent users use this skill to draft short-video spoken scripts, character stories, and personal-IP viewpoint scripts from a persona, pain point, or topic. The generated script follows a seven-step structure that emphasizes a contrast hook, suspense, story detail, viewpoint, elevation, and a punchline ending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security review reports that the spoken-script skill also directs agents to install and run a remote image-generation CLI with persistent dLazy credentials.

Mitigation: Review before installing, use only when dLazy CLI/API use is intended, and prefer a text-only variant when spoken-script generation does not require remote image generation.

Risk: Prompts and referenced media may be sent to dLazy services and API keys may be stored in local CLI configuration.

Mitigation: Avoid submitting sensitive content, rotate or revoke dLazy API keys as needed, and use per-session environment variables when local credential persistence is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown prose with optional step labels and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask clarifying questions before generation; image-generation command behavior uses dLazy CLI when the artifact's execution guidance is followed.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
