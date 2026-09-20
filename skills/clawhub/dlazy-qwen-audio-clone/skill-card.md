## Description:

Alibaba Bailian qwen3-tts voice cloning: upload a clean voice sample to clone a custom voice for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to invoke dLazy's hosted qwen-audio-clone service from an agent workflow, providing authorized voice audio and receiving a reusable cloned voice result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples and generated outputs are processed by dLazy cloud services and may be hosted on files.dlazy.com.

Mitigation: Use only voice audio the user is authorized to clone, and avoid submitting sensitive audio unless the applicable dLazy terms and data handling are acceptable.

Risk: A globally installed CLI persists on the user's system and the API key may be stored in the local dLazy configuration.

Mitigation: Prefer npx for one-off use when a persistent global install is unnecessary, rotate or revoke API keys from the dLazy dashboard, and use DLAZY_API_KEY per invocation when local key persistence is a concern.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs from files.dlazy.com or asynchronous task status for no-wait invocations.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
