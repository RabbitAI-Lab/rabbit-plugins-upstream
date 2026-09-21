## Description:

Moonshot AI thinking model with text, image, and video understanding for complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to send prompts, images, and videos through the dLazy CLI to the hosted Kimi K3 model for reasoning-heavy analysis, coding, and writing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy service.

Mitigation: Review the package before installation and use npx for non-persistent execution when appropriate.

Risk: Prompts and selected local media files may be sent to dLazy hosted endpoints.

Mitigation: Avoid sending sensitive data unless the user's data-handling requirements allow it.

Risk: A dLazy API key may be stored in local CLI configuration.

Mitigation: Use OS-level file protections, prefer per-invocation environment variables when needed, and rotate or revoke the key from dLazy if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON response from the dLazy CLI, with generated content or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input plus optional image and video references; async mode can return a generateId for polling.]

## Skill Version(s):

1.2.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
