## Description:

Moonshot AI thinking model with text, image, and video understanding for complex analysis, coding, and writing that need long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the hosted dLazy Kimi K3 model for long-reasoning text generation, multimodal understanding, coding help, and writing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected image, video, or audio files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive data unless the service is approved for that data, and review dLazy service terms before use.

Risk: Login may store a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation credentials or the npx form when appropriate, restrict local config access, and rotate or revoke the key from the dLazy dashboard if needed.

Risk: A global CLI install persists the dLazy package on the host.

Mitigation: Use the documented npx invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [JSON response with generated output objects, plus Markdown guidance and shell commands in agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, optional result saving, and user-selected image, video, or audio file inputs through the dLazy CLI.]

## Skill Version(s):

1.2.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
