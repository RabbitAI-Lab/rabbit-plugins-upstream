## Description:

Clone a custom voice for ElevenLabs text-to-speech by uploading a clean voice sample through dLazy's Instant Voice Cloning workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to create a custom ElevenLabs voice for text-to-speech from a clean voice sample they are authorized to use, then access the resulting voice through the dLazy workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded to dLazy for processing, which may involve privacy, retention, or service-cost considerations.

Mitigation: Use only recordings you have permission to clone, review dLazy's privacy practices and pricing, and avoid uploading sensitive audio.

Risk: The workflow uses a saved organization API key, which could be exposed if mishandled.

Mitigation: Protect the key and its local configuration, and do not share it in prompts, logs, or command output.

Risk: Some command examples may contain template errors.

Mitigation: Check the CLI help and confirm command arguments before running an example.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Audio]

**Output Format:** [Markdown guidance with shell command examples; the workflow returns voice-cloning results or task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice samples are uploaded for processing; asynchronous runs may return a task identifier and status.]

## Skill Version(s):

1.3.32 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
