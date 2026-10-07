## Description:

Helps agents upscale low-resolution images through dLazy's hosted service and return a link to the enhanced image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to restore or enlarge low-resolution image assets and obtain a hosted result URL or save the enhanced image locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Locally supplied images may be uploaded to dLazy, and enhanced results are hosted by dLazy.

Mitigation: Use only images approved for processing by this external service; review its data handling before submitting sensitive content.

Risk: Authentication may store an API key in the local CLI configuration.

Mitigation: Protect local credentials, or supply DLAZY_API_KEY per invocation when persistent storage is unsuitable.

Risk: The skill invokes a pinned third-party npm CLI.

Mitigation: Review the pinned package and its listed source before installation if the provider is not already trusted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source listed in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include a hosted enhanced-image URL; the CLI can optionally save the image locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.26 (source: ClawHub release evidence; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
