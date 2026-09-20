## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, supports text-to-image generation and image editing with reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to generate or edit images through the dLazy GPT Image 2.5 Flare CLI, including reference-image workflows, aspect-ratio selection, quality selection, and optional local download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input files can leave the local machine for processing by the third-party dLazy hosted service.

Mitigation: Avoid sensitive images or prompts unless the service is approved for that data and the user is comfortable with dLazy handling it.

Risk: Generated files are hosted by dLazy and returned through files.dlazy.com URLs.

Mitigation: Treat returned URLs and generated assets according to the user's data handling requirements before sharing or persisting them.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation credentials where appropriate, protect the local config file, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists a third-party package on the system.

Mitigation: Use the npx invocation form when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated image URLs; optional downloaded image file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a generateId for later polling; generated result URLs are hosted by files.dlazy.com.]

## Skill Version(s):

1.2.6 (source: ClawHub release evidence; artifact frontmatter pins the dLazy CLI package at 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
