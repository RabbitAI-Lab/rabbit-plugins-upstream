## Description:

全能视频生成 可灵 Kling V3 Omni helps agents use dLazy's Kling v3 Omni workflow to generate dynamic videos from prompts and image or video references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's Kling v3 Omni CLI for text-to-video, image-to-video, and reference-video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths supplied by the user are sent to dLazy hosted services, and local media inputs may be uploaded for generation.

Mitigation: Review prompts and media before invocation, avoid sending sensitive content unless approved for the dLazy service, and use only intended local file paths.

Risk: The dLazy API key is saved in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Use OS user permissions, prefer per-invocation environment variables where appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Using a globally installed third-party CLI can persist executable code on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred and review the CLI package/source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes for generated media URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; completed generations provide hosted media URLs and can be saved locally with --save.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
