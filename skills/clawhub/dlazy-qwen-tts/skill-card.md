## Description:

Helps agents generate speech from text with Alibaba Bailian Qwen3-TTS using system voices or custom voice descriptions through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can direct an agent to turn text into speech, select a system voice or describe a custom voice, and retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters and any user-provided media may be sent to dLazy's cloud service.

Mitigation: Avoid sensitive inputs unless their transfer to dLazy is acceptable.

Risk: The external CLI may persist an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials and consider npx @dlazy/cli@1.2.3 instead of a persistent global installation; review the package when handling sensitive data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio can be saved locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.29 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
