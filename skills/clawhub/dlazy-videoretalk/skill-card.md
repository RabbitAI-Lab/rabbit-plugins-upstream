## Description:

Video Retalk uses the dLazy CLI and hosted Tongyi VideoRetalk API to generate a talking-person video whose mouth movement matches a supplied audio track, with optional reference-image targeting for multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to run lip-sync video generation from a source talking-person video and replacement speech audio through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external @dlazy/cli package and hosted dLazy service.

Mitigation: Review the package and dLazy service terms before installation or use.

Risk: API credentials may be stored in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for temporary credential use when local credential persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Input video, audio, and reference-image files may be uploaded to dLazy media storage for processing.

Mitigation: Use only media that the user intends to upload to dLazy and avoid sensitive or unapproved content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with CLI commands; command results are JSON containing generated media URLs or asynchronous task identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Local video, audio, and reference-image paths may be uploaded to dLazy media storage when the CLI is invoked.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
