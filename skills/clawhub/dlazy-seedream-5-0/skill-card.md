## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate high-resolution images from prompts and optional reference images through dLazy's hosted Seedream 5.0 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files may be sent to dLazy's hosted service, and generated outputs may be hosted by dLazy.

Mitigation: Use the skill only with content appropriate for that service, and review dLazy's terms and data handling before sending sensitive prompts or media.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation credentials where appropriate, protect the local config file, and rotate or revoke the key from the dLazy dashboard if needed.

Risk: A persistent global CLI install may remain on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated image URLs or saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are hosted by dLazy unless saved locally with the CLI.]

## Skill Version(s):

1.2.14 (source: server release metadata; artifact frontmatter declares 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
