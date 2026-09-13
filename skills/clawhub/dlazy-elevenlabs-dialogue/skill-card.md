## Description:

Creates multi-voice ElevenLabs eleven_v3 dialogue audio by assigning different voices to dialogue lines and rendering the conversation in one run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content creators use this skill to generate character dialogue, podcast segments, and short skits with multiple voices from a single dialogue prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the third-party @dlazy/cli package and dLazy hosted API.

Mitigation: Prefer the pinned npx invocation, review the linked package or source before installing, and avoid a global install unless needed.

Risk: Dialogue prompts, parameters, and explicitly provided media files are sent to dLazy services.

Mitigation: Do not submit sensitive content unless that use is approved, and account for dLazy's service handling before deployment.

Risk: Authentication uses a dLazy API key that may be saved in local configuration or supplied through DLAZY_API_KEY.

Mitigation: Use a revocable key, prefer per-invocation DLAZY_API_KEY where practical, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The security guidance notes that the docs may need correction around output type and --inputs command syntax.

Mitigation: Verify generated commands with the CLI help or dry-run path before relying on them in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files, JSON]

**Output Format:** [Markdown instructions with bash commands; CLI responses are JSON and generated audio can be returned as hosted URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation, timeout control, dry-run cost estimates, and optional local save paths.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
