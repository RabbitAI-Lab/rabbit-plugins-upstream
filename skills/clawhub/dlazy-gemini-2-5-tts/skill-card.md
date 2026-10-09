## Description:

Helps agents generate natural-sounding Mandarin or English speech from text using Gemini 2.5 TTS through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ClawHub users can guide an agent to generate speech from text, choosing a language and voice for their audio content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are processed by dLazy's cloud API.

Mitigation: Avoid submitting sensitive text unless the cloud-processing arrangement is acceptable.

Risk: The dLazy CLI can store an API key locally.

Mitigation: Prefer a per-invocation DLAZY_API_KEY when appropriate; revoke or rotate stored keys when no longer needed.

Risk: The skill relies on a third-party CLI package.

Mitigation: Review the package and its source before installing in sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing a generated media URL or an asynchronous task ID.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
