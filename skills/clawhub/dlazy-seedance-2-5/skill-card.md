## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, multi-modal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to invoke dLazy's hosted Seedance 2.5 video generation service from an agent workflow, producing short-form videos from prompts and optional image, video, or audio references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy cloud endpoints for generation.

Mitigation: Use the skill only when cloud processing is acceptable, and avoid passing private media unless upload to dLazy is intended.

Risk: The dLazy API key is stored locally for CLI authentication.

Mitigation: Prefer per-invocation credentials or npx when persistence is not desired, and rotate or revoke the API key from the dLazy dashboard if exposure is suspected.

Risk: A global CLI install persists a tool on the local system.

Mitigation: Use the pinned npx invocation when a non-persistent execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing generated media URLs or an asynchronous task identifier.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
