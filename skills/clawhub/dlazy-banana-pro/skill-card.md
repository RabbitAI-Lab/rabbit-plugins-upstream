## Description:

Generates and edits images from text prompts and optional reference images using dLazy's hosted Nano Banana Pro service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input files are sent to dLazy, and generated files are hosted by dLazy.

Mitigation: Avoid submitting sensitive prompts or files unless the hosted service is acceptable for that content.

Risk: Authentication can store an API key locally.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: A global CLI installation persists on the device.

Mitigation: Use the pinned npx invocation if a global install is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON with hosted image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before images are ready.]

## Skill Version(s):

1.2.33 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
