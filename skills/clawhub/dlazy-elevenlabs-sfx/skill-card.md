## Description:

Generates 1-22 second sound effects from text prompts through the dLazy CLI's ElevenLabs SFX command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to generate short foley, ambience, alert, and game sound effects from text prompts, optionally saving the generated asset through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party CLI and hosted API, so prompts, parameters, and any referenced local media paths may be sent to dLazy services.

Mitigation: Review the pinned @dlazy/cli package before use, prefer npx @dlazy/cli@1.2.3 for on-demand execution, and avoid submitting sensitive prompts or files unless dLazy's terms and handling are acceptable.

Risk: Authentication may persist a dLazy API key in the user's CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local configuration is not desired, and rotate or revoke organization keys when needed.

Risk: The artifact's example output labels the generated asset as image/png even though this is a sound-effect skill.

Mitigation: Treat the example as a documentation inconsistency and verify actual generated output type before downstream processing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration instructions]

**Output Format:** [CLI command output JSON with generated asset URLs and optional saved local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
