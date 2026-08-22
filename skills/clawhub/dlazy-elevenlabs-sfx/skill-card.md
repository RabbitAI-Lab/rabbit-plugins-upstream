## Description:

Generates 1-22 second sound effects from text prompts using ElevenLabs text-to-sound through the dLazy CLI, for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short sound effects from natural-language prompts through the dLazy hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation parameters are sent to the dLazy hosted API for inference.

Mitigation: Use the skill only for content appropriate for a third-party cloud service and avoid sensitive prompts unless dLazy use is approved.

Risk: Authentication can persist a dLazy API key in ~/.dlazy/config.json.

Mitigation: Prefer per-invocation DLAZY_API_KEY when persistence is undesirable, verify local config file permissions, and rotate or revoke the key when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated output URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
