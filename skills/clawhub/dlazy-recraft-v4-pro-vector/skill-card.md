## Description:

High-fidelity text-to-vector generation for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Recraft V4 Pro Vector generator for vector-style image assets from prompts, with optional aspect ratio selection and local saving of generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided local files can be sent to the dLazy cloud service for generation.

Mitigation: Avoid submitting confidential or restricted content unless the intended use is approved under the provider's terms and your data-handling requirements.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Use per-run environment variables when persistent local storage is not desired, and rotate or revoke keys when access requirements change.

Risk: The skill depends on a pinned third-party npm CLI.

Mitigation: Review the package source and install the pinned CLI version from trusted package channels before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration instructions]

**Output Format:** [JSON containing generated asset metadata and hosted result URLs; optional local asset file when saved by the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated outputs are hosted remotely unless downloaded with the CLI save option.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
