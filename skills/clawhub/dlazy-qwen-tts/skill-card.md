## Description:

Generates speech from text with Qwen3-TTS using preset voices or a voice designed from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users generate spoken audio from text using preset voices, including dialects, or a custom voice description through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external npm CLI executes third-party software.

Mitigation: Review the CLI and use the version pinned by the skill before installing.

Risk: Speech prompts and selected parameters are sent to dLazy's hosted API.

Mitigation: Avoid submitting sensitive content unless the service is approved for it.

Risk: Signing in can save a dLazy API key locally.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: The TTS documentation includes an image-output example that may misstate the result format.

Mitigation: Verify the actual speech output and update the example before relying on it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can provide hosted audio results or save an asset locally; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
