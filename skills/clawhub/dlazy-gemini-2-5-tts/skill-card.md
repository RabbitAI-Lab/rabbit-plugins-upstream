## Description:

Generate multilingual, natural-sounding speech from prompts using dLazy's Gemini 2.5 text-to-speech CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Gemini 2.5 text-to-speech CLI for multilingual speech generation from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external npm CLI.

Mitigation: Use npx or an isolated environment when possible, avoid administrator-level npm execution, and review the referenced package source before installation.

Risk: Prompts and selected local media inputs are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive content unless the user accepts dLazy's service terms and data handling for the intended use.

Risk: Authentication relies on a dLazy API key stored locally or supplied through an environment variable.

Mitigation: Use a revocable organization-scoped API key and rotate or revoke it from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated results are returned as hosted file URLs, or as an async task ID when --no-wait is used.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
