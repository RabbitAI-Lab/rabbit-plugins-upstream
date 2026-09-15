## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for text-to-image and image editing, with support for reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy CLI using prompts, optional reference images, aspect-ratio controls, and quality settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local files may be sent to dLazy cloud services for generation.

Mitigation: Only provide prompts and files that are acceptable to upload to dLazy, and avoid sensitive or regulated content unless your organization has approved that use.

Risk: The skill depends on a dLazy API key stored locally or passed by environment variable.

Mitigation: Use a revocable API key, restrict local machine access, and rotate the key if the host or CLI installation is no longer trusted.

Risk: A global CLI installation may persist executable code in the user's environment.

Mitigation: Review the dLazy CLI source or package before installing in sensitive environments, and prefer npx or a sandboxed install when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration instructions]

**Output Format:** [JSON CLI output with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports prompts, up to five reference images, aspect ratio, quality, dry-run, async execution, timeout, and save-path options.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
