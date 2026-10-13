## Description:

Generates and edits images from prompts and optional reference images through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images with prompts and optional reference images, including work requiring detailed composition and in-image text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy, and generated files may be hosted there.

Mitigation: Avoid submitting sensitive prompts or media without approval; review dLazy's data handling before use.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect local credentials or supply the key per invocation through the DLAZY_API_KEY environment variable.

Risk: Installing a third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the pinned npm package and listed CLI source before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON metadata]

**Output Format:** [JSON response with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier instead of immediate image outputs.]

## Skill Version(s):

1.2.17 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
