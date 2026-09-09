## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn prompt text into natural speech through dLazy's hosted Doubao TTS wrapper, with selectable Chinese and English voices and speed settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and files provided to the skill are processed by dLazy's hosted service.

Mitigation: Avoid sending sensitive content unless hosted processing is intended and acceptable for the user's use case.

Risk: Using a globally installed npm CLI can increase local supply-chain exposure.

Mitigation: Prefer the pinned on-demand command npx @dlazy/cli@1.2.3 when a persistent global install is not needed.

Risk: The dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Keep the key scoped, revocable, and rotated through the dLazy dashboard when access no longer needs to persist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API Calls, Files]

**Output Format:** [JSON response with generated asset URLs, plus optional saved local output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, polling, dry runs, and optional local saving through the dLazy CLI.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
