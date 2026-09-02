## Description:

Grizzly by Yielding Bear provides one OpenAI-compatible key for 100+ LLMs with smart high/mid/free routing, semantic cache, and agent-ready install.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yieldingbear](https://clawhub.ai/user/yieldingbear)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Grizzly to configure an OpenAI-compatible LLM gateway, route requests across model tiers, and verify local setup for Hermes, OpenClaw, or shell environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer runs shell setup that stores a local API key.

Mitigation: Review the ClawHub artifact before installing, use a scoped Yielding Bear API key where available, and rotate or remove the key when it is no longer needed.

Risk: The setup can update the account's default routing or model settings.

Mitigation: Review the Yielding Bear dashboard after installation and confirm the active routing or model setting matches the intended agent behavior.

Risk: The installer can download SDK files into the user's home directory.

Mitigation: Prefer installing from the reviewed ClawHub artifact or inspect downloaded installer content before execution.

## Reference(s):

- [Yielding Bear product](https://yieldingbear.com)
- [Yielding Bear models](https://yieldingbear.com/models)
- [Yielding Bear docs](https://yieldingbear.com/docs)
- [ClawHub skill page](https://clawhub.ai/yieldingbear/skills/grizzly)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bash, curl, and a Yielding Bear API key for authenticated setup.]

## Skill Version(s):

2.4.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
