## Description:

Generate and edit high-quality images with Nano Banana 2.0, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate or edit images through the dLazy CLI with text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media are sent to dLazy's cloud API for processing.

Mitigation: Pass only prompts and files intended for dLazy, and review the cloud service before using sensitive data.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied by environment variable.

Mitigation: Use an organization-scoped key, keep it revocable, and rotate or revoke it from the dLazy dashboard when needed.

Risk: A global third-party CLI install persists an executable on the host.

Mitigation: Prefer on-demand npx execution or a sandbox when a persistent global install is not needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON, Files, Shell commands, Configuration instructions]

**Output Format:** [JSON responses with generated image URLs, optional downloaded image files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async runs can return a generateId for polling; saved outputs are written only when the caller supplies a save path.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
