## Description:

Generates 10-300 second original music with the ElevenLabs music_v1 model from natural-language prompts for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to request cloud-generated music from a prompt, optionally saving the returned media for background music, advertisements, and short-video soundtracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to persist a dLazy organization API key locally, and the security evidence says the claimed file-permission protection is not clearly enforced by the pinned CLI.

Mitigation: Prefer passing DLAZY_API_KEY per invocation, or verify that ~/.dlazy/config.json is readable only by the current user after login.

Risk: Prompts, parameters, and any file paths explicitly provided to the command may be sent to dLazy hosted services.

Mitigation: Review prompts and referenced files for sensitive content before invoking the skill.

Risk: A dLazy API key with paid credits or broad organization access can create cost or access exposure if mishandled.

Mitigation: Use the least-privileged organization key available and rotate or revoke the key from the dLazy dashboard when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON responses with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return async task metadata when --no-wait is used; --save can download the generated media asset.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
