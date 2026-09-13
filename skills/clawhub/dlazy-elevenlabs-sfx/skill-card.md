## Description:

ElevenLabs text-to-sound model that generates 1-22 second short sound effects from a description for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short sound effects through the dLazy CLI and ElevenLabs SFX model. It is suited for foley, ambience, alerts, and game sound-effect workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent global dLazy CLI install increases local supply-chain and maintenance exposure.

Mitigation: Use the pinned npx invocation when a persistent global binary is not needed, and review the linked dLazy CLI source before installation.

Risk: The dLazy API key is a credential that can authorize hosted generation requests.

Mitigation: Store it only in the intended local config or per-invocation environment, avoid sharing it, and rotate or revoke it if exposed.

Risk: Prompts, parameters, and selected local media files are sent to dLazy-hosted services for generation.

Mitigation: Submit only content intended for the hosted service and avoid passing local file paths containing sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated asset URLs or save generated files locally when requested; asynchronous calls can return a generation ID for polling.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
