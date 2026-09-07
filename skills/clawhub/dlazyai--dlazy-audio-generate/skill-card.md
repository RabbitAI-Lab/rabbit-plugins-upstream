## Description:

This skill helps agents generate speech, music, and sound effects through the dLazy CLI by selecting an appropriate audio or TTS model for the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to route audio-generation requests to an appropriate dLazy CLI model for text-to-speech, dialogue, music, voice search, or sound effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy hosted services for generation.

Mitigation: Use the skill only with data approved for external SaaS processing and avoid confidential media unless policy permits.

Risk: The skill depends on installing or invoking the third-party @dlazy/cli package.

Mitigation: Prefer the pinned npx invocation or a sandboxed install, and review the linked CLI source or npm package in sensitive environments.

Risk: A dLazy API key is required and may be stored in the local CLI configuration.

Mitigation: Protect the local config file and rotate or revoke the dLazy API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and CLI JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated results are returned through the dLazy CLI and may include hosted output URLs.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
