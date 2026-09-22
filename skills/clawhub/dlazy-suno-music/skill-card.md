## Description:

Suno music generation model for creating vocal or instrumental music in inspiration mode with automatic lyrics or custom mode with manual lyrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Suno music-generation service from an agent workflow, configure prompts and generation options, and receive generated music outputs or asynchronous task identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, selected local media files, and generated outputs through dLazy's hosted service.

Mitigation: Use it only with content appropriate for a third-party hosted API, and review data-handling expectations before sending sensitive prompts or files.

Risk: Authentication depends on a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use the documented dLazy login or auth flow, restrict local config access, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Global npm installation persists a third-party CLI on the system.

Mitigation: Prefer the pinned npx invocation when a persistent global install is not desired.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response with generated media URLs; optional saved media file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; --no-wait can return an asynchronous generateId for later polling.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
