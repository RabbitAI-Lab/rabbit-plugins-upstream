## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for text-to-image and image editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external agents use this skill to generate or edit images through the dLazy CLI using text prompts, optional reference images, aspect-ratio controls, and quality settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and image inputs may be uploaded to dLazy-hosted services.

Mitigation: Avoid sending sensitive media or prompts unless the user trusts the dLazy service terms and data handling.

Risk: Login can store a local dLazy API key in the CLI configuration.

Mitigation: Use OS-protected user configuration, rotate or revoke the key when needed, or provide the key per invocation with DLAZY_API_KEY.

Risk: A global CLI install persists third-party executable code on the system.

Mitigation: Use npx for on-demand execution when a persistent global install is not desired, and review the published CLI source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, Files, Guidance]

**Output Format:** [JSON containing generated image URLs, with optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task metadata when --no-wait is used; requires a dLazy API key.]

## Skill Version(s):

1.2.9 (source: server release evidence; artifact frontmatter declares 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
