## Description:

Uploads a clean voice sample to dLazy's Alibaba Bailian qwen3-tts voice-cloning service so agents can create a custom voice for later TTS calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to submit an authorized voice sample and create a named cloned voice for later text-to-speech workflows through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can misuse a person's voice or violate consent expectations.

Mitigation: Use only voice samples that the user owns or is explicitly authorized to clone, and confirm the intended TTS use is permitted.

Risk: Voice samples and generated assets may be sent to and hosted by dLazy services.

Mitigation: Treat uploaded audio and returned URLs as hosted service data, and review dLazy retention, deletion, and access terms before use.

Risk: Persistent CLI authentication can leave an API key saved in local configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or the npx path when avoiding a global install or saved key, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The documentation has mismatched command and output examples for an audio-cloning workflow.

Mitigation: Run the command help or dry-run mode and verify required parameters and returned JSON before automating downstream actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted output URLs or an asynchronous generateId for polling when no-wait mode is used.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
