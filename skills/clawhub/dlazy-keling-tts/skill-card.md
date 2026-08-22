## Description:

Converts text into high-quality, expressive speech using Kling TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Chinese or English speech from text through the pinned dLazy CLI and hosted Kling TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts are sent to the third-party dLazy API for generation.

Mitigation: Avoid submitting sensitive or private text unless it is intended for processing by the dLazy service.

Risk: Running dlazy login or dlazy auth set may store a dLazy API key in a local CLI configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when local persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Local files passed to media fields may be uploaded to dLazy media storage.

Mitigation: Do not pass private files unless upload to the service is intended and permitted.

Risk: A globally installed CLI can remain on the system after use.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when a persistent global CLI install is not needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-keling-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package; completed generations return hosted output URLs, while async runs return task IDs for polling.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
