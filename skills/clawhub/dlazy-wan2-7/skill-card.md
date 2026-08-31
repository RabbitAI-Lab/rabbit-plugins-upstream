## Description:

Tongyi Wanxiang 2.7 video model supports text-to-video, first/last-frame-to-video, and reference-to-video generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short videos from prompts and optional image, video, or audio references through dLazy's hosted Wan 2.7 workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media can be sent to dLazy cloud endpoints and may consume account credits.

Mitigation: Review prompt and media sensitivity before generation, confirm expected account cost, and use dry-run when estimating cost.

Risk: Authentication can save an API key in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys when access should change.

Risk: Using a globally installed CLI leaves a persistent binary on the system.

Mitigation: Use the documented npx invocation for on-demand execution when a persistent global install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON CLI output with generated media URLs, plus an optional saved media file when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when --no-wait is used.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
