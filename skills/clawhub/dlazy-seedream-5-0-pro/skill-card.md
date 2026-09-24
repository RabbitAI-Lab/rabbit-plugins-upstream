## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography, and complex composition for commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and agent workflows use this skill to call dLazy's Seedream 5.0 Pro image-generation CLI from prompts and optional reference images. It supports producing hosted image outputs or saved local assets for commercial visual and brand workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio inputs are sent to dLazy services for processing.

Mitigation: Provide only data appropriate for dLazy processing and review applicable account terms before use.

Risk: Authentication can store a dLazy API key in local CLI configuration until it is removed, rotated, or revoked.

Mitigation: Protect the local configuration file, prefer scoped keys, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on the third-party @dlazy/cli npm package.

Mitigation: Confirm trust in the dLazy CLI package and publisher before installing or running the pinned CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON responses containing generated image metadata and hosted output URLs; optional saved image files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key. Optional local media inputs are uploaded to dLazy services for processing.]

## Skill Version(s):

1.2.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
