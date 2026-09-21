## Description:

Alibaba's flagship Qwen reasoning model (2.4T-parameter MoE), strong at complex reasoning, code engineering and long-context analysis, with text and image input support through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the hosted dLazy Qwen 3.8 Max model for text generation, reasoning, code engineering, long-context analysis, and image-informed prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media files may be sent to dLazy cloud endpoints.

Mitigation: Use the skill only for content acceptable for dLazy processing, and avoid passing sensitive local files unless that transfer is intended.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use OS account protections for the config file, or pass DLAZY_API_KEY per invocation when persistent local storage is not desired.

Risk: Installing the CLI globally leaves a persistent binary on the system.

Mitigation: Prefer the pinned npx command when a non-global invocation is sufficient.

Risk: A saved or exposed dLazy API key could continue to authorize usage.

Mitigation: Rotate or revoke the key from the dLazy dashboard when access no longer needs to persist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON response from the dLazy CLI, with command-line guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task metadata when invoked with no-wait behavior; generated asset URLs are hosted by dLazy when applicable.]

## Skill Version(s):

1.2.14 (source: server release metadata; artifact frontmatter and install spec reference dLazy CLI 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
