## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate digital human broadcast videos from a portrait image plus audio or text through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party CLI and hosted API for generation.

Mitigation: Review the dLazy CLI package or source before installing in sensitive environments, and use the pinned npx invocation when avoiding a persistent global install.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for temporary credential use when appropriate, and rotate or revoke organization keys from the dLazy dashboard when access changes.

Risk: Local image, video, or audio inputs may be uploaded to dLazy media storage for cloud generation.

Mitigation: Only pass media files that are acceptable to upload to dLazy's service and avoid sensitive local files unless that upload is approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with CLI commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or save generated media files through the dLazy CLI.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
