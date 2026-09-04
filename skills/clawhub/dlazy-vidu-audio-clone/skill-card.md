## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Vidu Audio Clone service for voice cloning and text-to-speech generation from a prompt and optional reference audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced audio files may be uploaded to dLazy cloud endpoints for processing.

Mitigation: Use only audio and prompts that are authorized for upload to the third-party service, and review the service terms before use.

Risk: Authentication stores a dLazy API key in local CLI configuration unless a per-run environment variable is used.

Mitigation: Prefer per-invocation credentials when persistent local storage is not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact's output example appears to label the generated result as an image despite the audio-cloning purpose.

Mitigation: Treat the example as a documentation issue and verify actual CLI output shape before wiring downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing status, generated outputs, or asynchronous task details.]

## Skill Version(s):

1.3.12 (source: server-resolved ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
