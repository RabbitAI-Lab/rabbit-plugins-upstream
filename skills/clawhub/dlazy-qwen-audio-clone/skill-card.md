## Description:

Helps agents clone a custom voice from a voice sample for later text-to-speech use with Qwen3-TTS through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can provide a voice sample to create a custom voice for subsequent text-to-speech requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples can contain sensitive speech or be used to impersonate a person.

Mitigation: Upload only samples you have rights and consent to use, and avoid sensitive speech content.

Risk: Voice samples are sent to a third-party service with unclear retention and deletion terms.

Mitigation: Check dLazy's privacy, retention, and deletion terms before uploading real people's voices.

Risk: Authentication may save an API key locally.

Mitigation: Protect the local key or use DLAZY_API_KEY per invocation.

Risk: The documented examples and command options conflict, potentially causing incorrect calls.

Mitigation: Verify the actual command help before running the voice-cloning command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return JSON results or an asynchronous task ID.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; bundled skill files say 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
