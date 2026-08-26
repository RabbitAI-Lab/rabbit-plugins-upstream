## Description:

PixVerse C1 generates video from text prompts, images, first and last frames, or reference images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke PixVerse C1 via dLazy for cloud-hosted video generation from prompts and optional media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy services for generation.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable, avoid sensitive inputs, and review payloads before execution.

Risk: The dLazy API key may be stored in ~/.dlazy/config.json or supplied through DLAZY_API_KEY.

Mitigation: Prefer per-run environment variables when appropriate, check local config file permissions, and rotate or revoke keys that may have been exposed.

Risk: A broad video-generation trigger could cause unintended cloud generation attempts.

Mitigation: Use explicit invocation, review the CLI help, and use dry-run behavior when checking payloads or cost before calling the API.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI Repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown instructions with bash command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return generated media URLs, task IDs for asynchronous jobs, and optional saved local output files.]

## Skill Version(s):

1.2.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
