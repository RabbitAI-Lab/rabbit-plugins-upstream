## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Jimeng text-to-image outputs from prompts, optional reference images, and size parameters through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media files may be sent to dLazy hosted services.

Mitigation: Avoid using private files or sensitive prompt content unless the user accepts dLazy processing.

Risk: The dLazy CLI can store an API key in a local configuration file.

Mitigation: Use per-invocation credentials or the pinned npx command when a persistent global CLI or saved key is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI homepage from ClawHub metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Configuration instructions, Guidance]

**Output Format:** [JSON responses with generated image URLs, optional downloaded image files, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and sends prompts, selected media files, and generation parameters to dLazy-hosted services.]

## Skill Version(s):

1.3.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
