## Description:

Helps an agent clone a custom voice from a clean audio sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to submit a permitted voice sample for cloning and obtain a voice usable in text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a voice without the speaker's permission can enable impersonation or misuse.

Mitigation: Use only voice samples you own or have explicit permission to clone.

Risk: Uploaded voice samples and generated assets are processed by dLazy and its providers.

Mitigation: Confirm consent and data-handling requirements before submitting sensitive audio to the hosted service.

Risk: Examples and the documented output schema conflict with the voice-cloning options.

Mitigation: Check the installed CLI help and validate returned fields before relying on examples or automating downstream use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service may return a generated voice asset or an asynchronous task ID; verify actual CLI help and response fields.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
