## Description:

GPT Image 2 generates images from text and edits or synthesizes images from reference inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to create and edit images with GPT Image 2 through dLazy's hosted API and CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends saving a dLazy API key locally, while the security evidence notes that restricted file permissions may not be enforced by the installed CLI package.

Mitigation: Prefer DLAZY_API_KEY per invocation when persistent credentials are not needed, and protect or rotate locally stored API keys.

Risk: Prompts, parameters, and local reference image paths may be sent to dLazy services, and local images may be uploaded to dLazy storage.

Mitigation: Only submit prompts and files that are appropriate for third-party processing and storage under the user's dLazy organization.

Risk: The skill depends on a third-party hosted API and npm-distributed CLI for image generation.

Mitigation: Review dLazy's CLI source, npm package, service terms, and account credit state before installing or using the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON from the CLI containing generated image output URLs; optional saved image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload local reference images to dLazy storage.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
