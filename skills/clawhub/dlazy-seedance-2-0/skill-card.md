## Description:

Uses the dLazy CLI to call ByteDance Seedance 2.0 for text-to-video and reference-based video generation with image, video, audio, first-frame, and last-frame inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos through dLazy's hosted Seedance 2.0 service from prompts and optional multimodal reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy's hosted service.

Mitigation: Use the skill only with content appropriate for that service and avoid passing unintended local file paths.

Risk: The dLazy CLI can store an API key in the user's local configuration.

Mitigation: Use scoped credentials where possible, protect the local config file, and rotate or revoke keys when access changes.

Risk: A global installation persists a third-party CLI on the system.

Mitigation: Use the pinned npx invocation for one-off use when a persistent global binary is not desired.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or an async task ID depending on CLI flags.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
