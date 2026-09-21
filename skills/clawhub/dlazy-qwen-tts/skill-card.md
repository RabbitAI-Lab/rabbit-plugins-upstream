## Description:

Alibaba Bailian qwen3-tts text-to-speech lets agents choose curated system voices, including dialect voices, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Qwen TTS speech through the dLazy CLI, choosing a preset voice or describing a custom voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and sends prompts and selected parameters to dLazy's hosted service.

Mitigation: Review the service fit for the data being submitted and avoid sending sensitive content unless the environment permits that SaaS workflow.

Risk: Installing the CLI globally leaves a persistent third-party binary on the host.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred, or review @dlazy/cli@1.2.3 before global installation.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Store the key only in approved environments and rotate or revoke it from the dLazy dashboard when access should end.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted generated asset URLs, async task identifiers, or saved local output files through the dLazy CLI.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
