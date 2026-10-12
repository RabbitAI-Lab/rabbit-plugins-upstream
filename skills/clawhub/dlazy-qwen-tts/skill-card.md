## Description:

Generates speech from text with Qwen TTS using preset voices or a voice designed from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users create spoken audio from text, choosing a preset voice or describing a custom voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party CLI.

Mitigation: Review the pinned @dlazy/cli package before installation or execution.

Risk: Prompts are sent to dLazy's cloud service and generated files are hosted there.

Mitigation: Avoid sending sensitive text unless the service's data handling is acceptable for the task.

Risk: Logging in stores a dLazy API key in local configuration.

Mitigation: Protect the local key or provide DLAZY_API_KEY per invocation instead.

Risk: The documented output example shows a PNG image rather than audio.

Mitigation: Confirm the actual audio response format before relying on the example.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata (not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio may be available through a hosted URL or saved locally; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub server release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
