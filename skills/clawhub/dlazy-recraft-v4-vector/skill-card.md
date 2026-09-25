## Description:

Text-to-vector model that generates scalable design assets such as logos and icons through the dLazy Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agent users use this skill to request vector-style image assets from the hosted dLazy Recraft V4 Vector API and optionally save the returned asset locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media files explicitly supplied to the skill may be sent to the dLazy hosted service.

Mitigation: Use the skill only with data approved for dLazy processing, and avoid passing sensitive prompts or files unless permitted by the user's organization.

Risk: Generated outputs are hosted on files.dlazy.com.

Mitigation: Review generated asset URLs before sharing them and download outputs to controlled storage when retention or access controls matter.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-user credentials, protect the local config file, and rotate or revoke the key from the dLazy dashboard if it may be exposed.

Risk: Evidence notes a documentation mismatch about whether results are SVG/vector or PNG/raster.

Mitigation: Inspect the returned MIME type and saved asset before relying on the output as true vector artwork.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated asset URLs; optional downloaded image file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous runs may return a generateId for polling instead of immediate outputs.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
