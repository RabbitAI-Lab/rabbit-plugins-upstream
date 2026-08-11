## Description:

Synthesize text into natural, fluent speech using Doubao TTS through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate Chinese or English speech from text prompts with selectable voices and speed settings through dLazy's Doubao TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and supported local-file inputs may be sent to the dLazy/Doubao hosted service for processing.

Mitigation: Avoid submitting sensitive text or local files unless cloud processing by the service is intended.

Risk: The skill requires a dLazy API key, which may be stored in the local CLI configuration.

Mitigation: Use `DLAZY_API_KEY` for per-invocation credentials or rotate and revoke keys from the dLazy dashboard when access changes.

Risk: Global CLI installation persists a third-party executable on the system.

Mitigation: Use the pinned `npx @dlazy/cli@1.2.3` invocation when a non-persistent CLI is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated speech results are returned as hosted file URLs; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
