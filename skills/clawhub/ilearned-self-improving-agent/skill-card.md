## Description:

Use when an OpenClaw, LobeHub, or Hermes assistant encounters user corrections, failed commands or tools, outdated knowledge, missing capabilities, recurring mistakes, or a better approach, and before tasks where past lessons may matter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrywang121](https://clawhub.ai/user/jerrywang121)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using OpenClaw, LobeHub, or Hermes can capture reusable lessons from corrections and verified failures, retrieve relevant rules before acting, and refine rules based on observed outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled instructions do not verify the behavior of the external ilearned runtime package.

Mitigation: Review the package and version before approving installation, and verify live tool calls before relying on the integration.

Risk: Lessons or exported data may contain sensitive information; JSONL exports remain plaintext even when database encryption is enabled.

Mitigation: Use private storage, keep sensitive information out of lessons, and protect export files separately.

## Reference(s):

- [Server-resolved source release](https://github.com/jerrywang121/ilearned/tree/main/example/skills/ilearned-self-improving-agent)
- [Setup and operations](references/setup-and-operations.md)
- [ilearned MCP tools](https://github.com/jerrywang121/ilearned/blob/main/docs/mcp.md)
- [ilearned CLI and configuration](https://github.com/jerrywang121/ilearned/blob/main/docs/cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands, configuration examples, and structured lesson fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scoped, reusable lessons with verification guidance; setup depends on an installed and connected ilearned service.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
