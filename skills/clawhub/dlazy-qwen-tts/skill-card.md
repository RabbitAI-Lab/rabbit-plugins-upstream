## Description:

Helps agents use dLazy's Qwen3 text-to-speech service with preset voices or a voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to prepare text-to-speech requests with a preset or custom-described voice and retrieve generated speech through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the external dLazy CLI executes third-party software.

Mitigation: Review the pinned CLI package and its source before installing or running it.

Risk: Prompts are sent to dLazy's hosted API, and an API key is stored locally.

Mitigation: Avoid submitting sensitive content, protect the locally stored key, and rotate or revoke it if exposed.

Risk: The sample response shows image output despite the text-to-speech use case.

Mitigation: Check actual output behavior with `dlazy qwen-tts -h` or a dry run before relying on the example.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI reports JSON with a generated result URL or an asynchronous task ID; the documented sample output may not reflect speech output.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
