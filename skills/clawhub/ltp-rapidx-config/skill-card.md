## Description:

Use when an agent needs to install or configure RapidX CLI/MCP access, set production LTP credentials, locate the agent workspace MCP config, review integration, discover tools, or run read-only self-checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liquiditytech](https://clawhub.ai/user/liquiditytech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install or upgrade RapidX CLI, configure CLI or MCP access, handle RapidX credentials, verify runtime readiness, and produce masked integration reviews before trading workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install mutable npm code through the RapidX CLI package.

Mitigation: Install only when the npm publisher is trusted; prefer a workspace-local, pinned CLI version where operationally feasible.

Risk: MCP configuration can persist live production LTP credentials.

Mitigation: Use host-native secret references or an OS/enterprise secret manager; if literals are unavoidable, use least-privilege credentials, owner-only file permissions, keep configs out of repositories and sync systems, and rotate keys after exposure concerns.

## Reference(s):

- [RapidX Capability Overview](artifact/references/capability-overview.md)
- [RapidX Skills / CLI / MCP Best Practices](artifact/references/best-practices.md)
- [ClawHub Skill Page](https://clawhub.ai/liquiditytech/skills/ltp-rapidx-config)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON/YAML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Masks credentials in reviews and classifies runtime readiness from observed CLI or MCP evidence.]

## Skill Version(s):

1.0.17 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
