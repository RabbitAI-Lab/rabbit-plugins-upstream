## Description:

A comprehensive generation skill that helps an agent select and run dLazy CLI models for image, video, and audio generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to route image, video, and audio generation requests to an appropriate dLazy CLI model, configure authentication, and run generation commands against the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs the third-party dLazy npm CLI.

Mitigation: Install only when the dLazy CLI and service are trusted; use npx for per-invocation execution when a persistent global install is not desired.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY for ephemeral use, and rotate or revoke the key if the package or host environment is in doubt.

Risk: Prompts and referenced image, video, or audio files may be sent to dLazy services for generation.

Mitigation: Treat prompts and media paths as data shared with dLazy, and avoid submitting sensitive content unless that service use is approved.

Risk: Generation relies on a paid third-party service and can fail when credits or authorization are unavailable.

Mitigation: Check authentication and account credit status before depending on the skill in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline bash commands; dLazy CLI commands return JSON envelopes and hosted media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; generation requests may send prompts and referenced media files to dLazy endpoints.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
