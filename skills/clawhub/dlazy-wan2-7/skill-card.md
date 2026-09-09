## Description:

Tongyi Wanxiang 2.7 video generation skill covering text-to-video, first/last-frame-to-video, and reference-guided video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's Wan 2.7 CLI for video generation from prompts and optional image, video, or audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media may be sent or uploaded to dLazy services.

Mitigation: Use the skill only for content intended for dLazy processing, and review the third-party service terms before invoking it with sensitive media.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY when persistence is not desired, and rotate or revoke organization keys when access should change.

Risk: A global npm install leaves the dLazy CLI installed beyond a single task.

Mitigation: Prefer the pinned npx invocation or an isolated environment when less persistence is desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or save generated media to a requested local path.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
