## Description:

Generate and edit images with Nano Banana Pro through the dLazy CLI, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate or edit images through dLazy's hosted Nano Banana Pro service. It is useful for text-to-image and image-to-image creation when the user can provide a dLazy API key and is comfortable uploading prompts and referenced media to dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and referenced media files to dLazy's hosted API and file storage.

Mitigation: Use it only for prompts and media you are willing to upload to dLazy, and avoid confidential or regulated content unless your organization has approved that service path.

Risk: The dLazy CLI requires an API key stored in local configuration or supplied by environment variable.

Mitigation: Use a revocable API key, rotate or revoke it from the dLazy dashboard when needed, and prefer per-user credential storage with restricted file permissions.

Risk: Installing a global npm CLI persists executable code on the system.

Mitigation: Prefer the documented pinned npx invocation when possible, or review the linked package and source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result objects containing generated image URLs or async task identifiers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as files.dlazy.com URLs and can be downloaded locally with the CLI save option.]

## Skill Version(s):

1.2.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
