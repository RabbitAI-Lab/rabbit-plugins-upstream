## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a static character image, with an optional reference video and prompt, into an action video through the dLazy-hosted Jimeng Dream Actor service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy/Jimeng for cloud processing.

Mitigation: Use the skill only when cloud upload is acceptable, review selected files before invocation, and prefer dry-run for first use.

Risk: The skill uses a persisted dLazy API key and may spend dLazy credits.

Mitigation: Protect or rotate the saved API key on shared machines, and confirm expected cost before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated media URLs, async task IDs, and optional saved local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimates, asynchronous polling, and downloading generated assets with --save.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
