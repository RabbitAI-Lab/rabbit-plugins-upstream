## Description:

ElevenLabs text-to-sound model that generates 1-22 second sound effects from a description for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to call the dLazy-hosted ElevenLabs sound-effect generator from text prompts and save or reference generated short audio assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key can be persisted in the local CLI config and may control paid credits or organization resources.

Mitigation: Use DLAZY_API_KEY per run when persistent credentials are not desired; if credentials are saved, check ~/.dlazy/config.json permissions and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and supplied media paths are sent to dLazy cloud endpoints for generation and hosted output delivery.

Mitigation: Avoid submitting confidential prompts or media unless the user has reviewed the dLazy service terms and accepts cloud processing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance, audio asset URLs]

**Output Format:** [Markdown guidance with shell commands and JSON API-result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted URLs and may be saved locally with the CLI --save option.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
