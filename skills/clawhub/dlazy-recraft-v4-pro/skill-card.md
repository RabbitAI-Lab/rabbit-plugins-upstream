## Description:

Generates 4MP raster images for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate high-resolution raster artwork from text prompts for print and large-format assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media can be sent to dLazy, and generated files are hosted there.

Mitigation: Avoid submitting sensitive content unless the dLazy service and its handling of data meet your requirements.

Risk: Logging in can save an API key in local configuration.

Mitigation: Use a per-invocation API key when persistent storage is undesirable; protect and rotate keys as needed.

Risk: Generating images may consume paid credits, and using the CLI may require npm installation.

Mitigation: Review the cost estimate with dry-run and confirm you trust the dLazy CLI before installing or invoking it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON results, Image links]

**Output Format:** [Text guidance and JSON containing a hosted image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local image download; asynchronous jobs return a task ID.]

## Skill Version(s):

1.3.22 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
