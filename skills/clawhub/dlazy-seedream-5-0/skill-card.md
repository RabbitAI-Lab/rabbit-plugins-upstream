## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print uses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted image-generation CLI for prompt-based and reference-image generation at 2K, 3K, or 4K resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files may be sent to dLazy servers for image generation.

Mitigation: Avoid submitting sensitive content unless the user's data-handling requirements allow third-party cloud processing.

Risk: The skill relies on a third-party CLI and hosted API.

Mitigation: Review the dLazy CLI source and service terms before installation or deployment.

Risk: A dLazy API key is required and may be stored in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where appropriate, or verify private permissions on the local configuration file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses containing generated image URLs; optional saved image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload user-provided reference files to dLazy media storage for generation.]

## Skill Version(s):

1.2.7 (source: server release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
