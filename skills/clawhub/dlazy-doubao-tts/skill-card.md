## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate Chinese or English speech from text through the dLazy Doubao TTS command-line workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and hosted text-to-speech API that receives submitted text.

Mitigation: Confirm trust in the dLazy CLI and service before use, and avoid sending sensitive text unless that is acceptable for the intended use case.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A persistent global npm binary may be installed on the user's system.

Mitigation: Prefer npx or a sandboxed environment when a temporary, non-global CLI invocation is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces hosted audio result URLs and can save generated assets locally when requested.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
