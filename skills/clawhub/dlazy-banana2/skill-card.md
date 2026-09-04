## Description:

Generates and edits high-quality images with Nano Banana 2.0, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Nano Banana 2 image generation and editing service from an agent or shell workflow using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media can be uploaded to dLazy's hosted service.

Mitigation: Install and use this skill only when the user intends to use dLazy's cloud service, and avoid sending sensitive prompts or media unless approved for that service.

Risk: The dLazy organization API key can be stored in a local CLI configuration file.

Mitigation: Prefer per-run DLAZY_API_KEY use when practical, or verify that ~/.dlazy/config.json is restricted to the local OS user after login or auth setup.

Risk: API calls may consume dLazy credits.

Mitigation: Use --dry-run for payload and cost estimates when appropriate, and confirm credit-impacting actions before running generation for users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI responses are JSON containing generated image URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return cloud-hosted image URLs from files.dlazy.com or save generated assets to a local path when --save is used.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
