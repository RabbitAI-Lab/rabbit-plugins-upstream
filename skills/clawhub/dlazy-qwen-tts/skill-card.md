## Description:

This skill lets agents generate Alibaba Bailian qwen3-tts speech from text using curated system voices or a natural-language voice description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's Qwen TTS command, choose voice and language options, and receive speech-generation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media can be sent to the dLazy hosted service for generation.

Mitigation: Submit only content that is appropriate for the dLazy service and avoid sensitive prompts or files unless approved for that environment.

Risk: A global CLI install and saved API key can persist credentials and executable code on the user's machine.

Mitigation: Use the pinned npx invocation when a persistent install is not desired, and rotate or revoke saved API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned by the dLazy CLI as hosted file URLs or can be saved to a local path.]

## Skill Version(s):

1.3.11 (source: release evidence; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
