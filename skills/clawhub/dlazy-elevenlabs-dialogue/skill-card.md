## Description:

Generates multi-voice ElevenLabs dialogue audio through the pinned dLazy CLI, allowing an agent to assign different voices to dialogue lines and save or return generated results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent workflows use this skill to generate spoken multi-character dialogue for podcasts, short scenes, character scripts, and similar audio assets through a hosted dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text and explicitly supplied media paths may be sent to the third-party dLazy hosted service for generation.

Mitigation: Avoid submitting sensitive dialogue or media unless the dLazy service terms and data handling are acceptable for the use case.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials or rotate and revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party npm CLI package and hosted endpoints.

Mitigation: Use the pinned install or npx command, review the CLI source/package before installation, and account for endpoint availability.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio results are returned by the dLazy CLI as hosted asset URLs and may be saved locally with the --save option.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
