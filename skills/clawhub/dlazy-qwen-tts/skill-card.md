## Description:

Generates text-to-speech audio with Alibaba Bailian Qwen3-TTS using curated system voices or a custom voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to synthesize speech from prompt text through the dLazy Qwen TTS CLI, choosing a system voice, language, or custom voice description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected inputs are sent to dLazy's hosted service for text-to-speech generation.

Mitigation: Use the skill only for inputs the user is comfortable sending to dLazy, and avoid sensitive content unless third-party processing is acceptable.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use the npx path or DLAZY_API_KEY per invocation for less local persistence, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI project link from release metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated asset URLs, async task identifiers, and saved local files when the CLI save option is used.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
