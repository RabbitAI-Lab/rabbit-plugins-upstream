## Description:

Image replicate tool: analyzes the visuals, composition, colors, lighting, and style of the source image, builds a replicate prompt, and hands it off to Seedream 4.5 to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to analyze a reference image and generate a new image with similar visual style through dLazy's hosted image-replication service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media are uploaded to dLazy's hosted API for inference.

Mitigation: Use only prompts and media approved for dLazy upload, and avoid confidential inputs unless covered by the user's organization policy.

Risk: Generated files may be hosted on dLazy media storage.

Mitigation: Treat returned file URLs as third-party hosted assets and review sharing or retention expectations before distributing outputs.

Risk: Login can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer the pinned npx command for non-persistent CLI use, protect the local config file, and rotate or revoke the API key if it may be exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown instructions with bash command examples and JSON response envelopes; generated assets are returned as image URLs or saved files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; supports async task IDs and local result saving through the dLazy CLI.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
