## Description:

MyBooks TTS helps administrators configure MiMo or OpenAI-compatible text-to-speech, convert EPUB books into audiobooks, track conversion progress, and manage cloned voices and voice prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiningsprk-arch](https://clawhub.ai/user/shiningsprk-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and MyBooks administrators use this skill to manage text-to-speech settings and audiobook conversion workflows for a MyBooks server. It can configure API credentials, start EPUB conversion jobs, inspect progress, and manage cloned voice samples and prompt descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles MyBooks administrator credentials and TTS API keys.

Mitigation: Provide credentials through session-scoped environment variables and use the skill only with a MyBooks server and admin account you control.

Risk: Conversion, cloned voice, and prompt operations can make persistent server-side changes.

Mitigation: Confirm book IDs, API keys, cloned voice names, and prompt names before running write or delete operations.

Risk: Clone voice workflows may involve sensitive or permissioned audio samples.

Mitigation: Upload only voice samples you have permission to use and monitor server storage after uploads and conversions.

Risk: Downloaded clone audio can be written to arbitrary local paths supplied by the user.

Mitigation: Save downloaded audio only to a scratch or output directory intended for generated files.

## Reference(s):

- [Server-resolved source provenance](https://github.com/shiningsprk-arch/mybooks-tts-skill/tree/main/skills/mybooks_tts)
- [ClawHub skill listing](https://clawhub.ai/shiningsprk-arch/skills/mybooks-tts)
- [MyBooks homepage](https://www.mybooks.top)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance, Files]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save cloned voice preview audio to a local file when requested.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
