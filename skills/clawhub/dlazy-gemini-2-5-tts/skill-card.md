## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate Chinese or English speech from text through the dLazy Gemini 2.5 TTS CLI integration. It supports selecting voice language and voice style, using dry-run estimates, and polling asynchronous generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input files may leave the user's machine for hosted text-to-speech processing.

Mitigation: Review prompt and file contents before use, avoid sending sensitive data unless approved, and use dry-run when evaluating cost or payload shape.

Risk: The dLazy API key may be stored locally and used for paid credits.

Mitigation: Protect the local CLI config, prefer per-invocation environment variables for temporary use, and rotate or revoke the API key if exposed.

Risk: Generated outputs are hosted by dLazy and returned as external URLs.

Mitigation: Treat output links as third-party hosted artifacts and review sharing, retention, and access expectations before distributing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is returned as hosted output URLs; asynchronous calls may return a task identifier for later polling.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
