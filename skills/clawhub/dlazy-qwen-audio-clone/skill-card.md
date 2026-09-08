## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to clone a custom voice usable in later text-to-speech calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the dLazy qwen-audio-clone CLI, upload a clean audio sample and metadata, and create a custom voice for subsequent text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing or running the @dlazy/cli npm package.

Mitigation: Install only if you trust dLazy and the package; prefer npx or another isolated install over a global install and avoid elevated privileges.

Risk: The CLI stores or accepts a dLazy API key for hosted API access.

Mitigation: Use a revocable API key, protect the local CLI config, or pass DLAZY_API_KEY per invocation when appropriate.

Risk: Audio files passed to the skill are uploaded to dLazy's hosted service.

Mitigation: Only pass audio files intended for upload and review the service terms before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash command examples and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or asynchronous task identifiers from files.dlazy.com.]

## Skill Version(s):

1.3.13 (source: release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
