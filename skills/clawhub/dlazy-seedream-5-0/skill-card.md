## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-resolution images from text prompts and optional reference images for visuals, posters, and print-oriented creative work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and provided local media files are sent to the dLazy hosted API and media storage for generation.

Mitigation: Only provide prompts and files intended for upload, and review the dLazy service terms for the target use case.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration.

Mitigation: Treat the key as an account credential, use per-invocation environment variables when appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global npm install persists the dLazy CLI on the local system.

Mitigation: Review the linked CLI source before installing or use the pinned npx command for on-demand execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown instructions with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results are returned as hosted image URLs and can optionally be saved to a local path; asynchronous runs return a task identifier for polling.]

## Skill Version(s):

1.2.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
