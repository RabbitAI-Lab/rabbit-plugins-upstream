## Description:

Generates 4MP high-resolution raster images for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request cloud-hosted Recraft V4 Pro image generation through the dLazy CLI, including optional saving of generated image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected local files are sent to dLazy's hosted service for generation.

Mitigation: Use the skill only with content that is appropriate to process through dLazy's cloud service.

Risk: Authentication may store a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation credentials when preferred, and rotate or revoke the API key from dLazy if exposure is suspected.

Risk: A global CLI installation persists tooling on the local system.

Mitigation: Use the documented npx invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as dLazy-hosted image URLs and may be saved locally when the CLI save option is used.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
