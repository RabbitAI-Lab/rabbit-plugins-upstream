## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Seedream 5.0 image generation from an agent, including prompt-based generation, reference-image workflows, high-resolution output, and optional local saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and hosted dLazy API.

Mitigation: Review the package and source references before installation, and install only in environments where third-party CLI execution is acceptable.

Risk: Prompts and generation parameters are sent to dLazy for inference.

Mitigation: Avoid submitting confidential or regulated text unless the user's dLazy terms and data handling requirements allow it.

Risk: Reference images explicitly passed to the CLI may be uploaded to dLazy storage.

Mitigation: Pass only files approved for upload to dLazy, and prefer generated URLs or local saves according to the user's data-retention needs.

Risk: Authentication can save a dLazy API key in local CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [JSON response with generated image URLs, optional local image files, and command-line status or error messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, polling, cost dry runs, and saved output paths through the dLazy CLI.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
