## Description:

Helps agents generate speech with Alibaba Bailian Qwen3-TTS using preset voices or a custom voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to request text-to-speech with a preset voice or a voice designed from a description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly supplied media files are sent to dLazy's hosted service.

Mitigation: Confirm the service is trusted before sending sensitive prompts or media.

Risk: Using the CLI requires an API key that can be stored locally.

Mitigation: Protect the key and rotate or revoke it when no longer needed.

Risk: Installing a third-party CLI introduces executable software to the user's environment.

Mitigation: Review the dLazy CLI before installing; use the documented on-demand invocation if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked service returns JSON with generated-asset links; an optional command saves the asset locally.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
