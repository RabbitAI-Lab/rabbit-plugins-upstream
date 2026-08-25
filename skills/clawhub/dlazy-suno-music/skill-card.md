## Description:

Generates Suno music through dLazy in inspiration or custom mode, with options for manual lyrics, vocals or instrumentals, style controls, asynchronous generation, and saved outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate music with dLazy's Suno wrapper, configure lyrics and style parameters, authenticate with a dLazy API key, and retrieve generated audio assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and explicitly supplied media files may be sent to dLazy's hosted service.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable for the user's data and avoid submitting sensitive media or prompts unless approved.

Risk: Authentication can persist a dLazy API key in a local CLI configuration file.

Mitigation: Use DLAZY_API_KEY or npx for less persistent use when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Generated assets are returned as URLs hosted by dLazy.

Mitigation: Review sharing, retention, and access expectations before using generated output URLs in downstream workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions]

**Output Format:** [JSON responses with generated asset URLs, task status metadata for asynchronous runs, and optional downloaded files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
