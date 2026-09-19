## Description:

Generate dynamic videos based on a single first frame image and prompts using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to generate short Jimeng image-to-video clips from a first-frame image and prompt through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and image inputs may be sent to dLazy hosted API and media storage.

Mitigation: Use the skill only with inputs that are appropriate for the dLazy hosted service and avoid sending sensitive files or prompts unless the user has approved that handling.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Prefer least-privilege API keys where available, keep local config access restricted, and rotate or revoke keys from the dLazy dashboard when access is no longer needed.

Risk: The skill installs or invokes a pinned npm CLI package.

Mitigation: Review the pinned @dlazy/cli package and source before global installation, or use the pinned npx invocation for per-run use.

Risk: The artifact documentation has inconsistent examples for the input flag and output type.

Mitigation: Use the command help and declared --firstFrame option as the operational reference before running production jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON responses with hosted output URLs; optional downloaded result files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task metadata when --no-wait is used.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
