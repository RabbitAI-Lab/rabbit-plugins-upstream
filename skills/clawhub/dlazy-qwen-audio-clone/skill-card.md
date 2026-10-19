## Description:

Clones a custom voice from a clean audio sample for use in subsequent Qwen3-TTS speech generation through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to submit a consented voice sample and create a reusable custom voice for text-to-speech generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples may be uploaded to dLazy-hosted endpoints.

Mitigation: Use samples only with proper consent and confirm you trust the service before uploading.

Risk: The published command and output examples contain modality mistakes.

Mitigation: Verify the live qwen-audio-clone help and returned output before relying on the examples.

Risk: Installing and running the third-party CLI executes external software.

Mitigation: Review and trust the CLI before installation; use the pinned npx form if a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell examples and illustrative JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return a result URL or an asynchronous task ID; verify actual audio-cloning output before use.]

## Skill Version(s):

1.3.30 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
