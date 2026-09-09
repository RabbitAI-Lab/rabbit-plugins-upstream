## Description:

Generates 1-22 second ElevenLabs sound effects from text prompts for foley, ambience, alerts, and game audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the pinned dLazy CLI for short sound-effect generation from text prompts, including foley, ambience, alerts, and game SFX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a pinned third-party dLazy CLI and hosted service.

Mitigation: Install only after reviewing the linked source or package, and prefer npx @dlazy/cli@1.2.3 when a persistent global binary is not needed.

Risk: The dLazy API key is a credential stored in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Use a revocable organization key, restrict local config access, and rotate or revoke the key when access is no longer needed.

Risk: Prompts and intentionally supplied local media paths are sent to api.dlazy.com or uploaded to files.dlazy.com for cloud processing.

Mitigation: Pass only prompts and files intended for the dLazy service, and avoid submitting sensitive or unauthorized content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated asset URLs; optional saved asset file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and uses the pinned @dlazy/cli 1.2.3 package.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
