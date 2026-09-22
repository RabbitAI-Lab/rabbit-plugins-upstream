## Description:

Generates 1MP raster images with Recraft V4 for everyday creative work and rapid design iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative workers, designers, developers, and agents use this skill to request Recraft V4 image generation through the dLazy CLI and receive generated image assets or hosted result URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any input files passed to the CLI may be sent to dLazy cloud services, and generated outputs may be hosted by dLazy.

Mitigation: Review prompts and files for sensitive content before use, and avoid submitting material that should not be processed or hosted by a third-party cloud service.

Risk: The skill depends on a third-party npm CLI and a locally stored or environment-provided API key.

Mitigation: Install only the pinned CLI version from trusted package sources, protect the local dLazy configuration, and rotate or revoke the API key when access should change.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)

## Skill Output:

**Output Type(s):** [JSON, Files, API Calls, Shell commands, Configuration instructions]

**Output Format:** [JSON response with generated image metadata, hosted image URLs, and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and input files provided to the CLI may be sent to dLazy cloud endpoints.]

## Skill Version(s):

1.3.19 (source: evidence.release.version; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
