## Description:

Generate matching scene sound effects based on text descriptions or video frames using Kling SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to ask an agent to generate scene-matched sound effects from text prompts or a referenced video through the dLazy Kling SFX service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced video or media files are sent to dLazy's hosted service for generation.

Mitigation: Use the skill only for prompts and media that are appropriate to send to the dLazy service, and avoid submitting sensitive or restricted content.

Risk: The dLazy API key may be stored in the local CLI configuration when using the login or auth commands.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when preferred, and rotate or revoke API keys from the dLazy dashboard when no longer needed.

Risk: A global CLI install persists the dLazy binary on the user's system.

Mitigation: Use the pinned npx invocation when a temporary command execution is preferable to a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-keling-sfx)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON results that include hosted generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation by returning a generateId for later polling.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
