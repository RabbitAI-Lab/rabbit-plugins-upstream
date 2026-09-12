## Description:

Generate high-quality images with Doubao Seedream 4.5 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to have an agent generate images or transform supplied images through dLazy's hosted Seedream 4.5 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party npm CLI and hosted dLazy API.

Mitigation: Review the dLazy CLI source or npm package before use, and prefer npx when a persistent global install is not desired.

Risk: Prompts and selected media files are sent to dLazy endpoints for generation.

Mitigation: Only provide prompts and files intended for upload to dLazy.

Risk: API keys are stored locally or supplied through the DLAZY_API_KEY environment variable.

Mitigation: Rotate or revoke the dLazy API key if it may have been exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs or asynchronous task identifiers from dLazy.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
