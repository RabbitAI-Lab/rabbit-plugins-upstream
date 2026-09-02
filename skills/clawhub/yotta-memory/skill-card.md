## Description:

元忆 yotta-memory gives AI agents boundary-aware, file-based long-term memory with local Markdown storage, recall/context workflows, public FACT sharing, and private PREF/BOUND/COMMIT isolation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, power users, and agent operators use this skill to let AI agents persist and retrieve cross-session context while keeping public facts separate from private preferences, boundaries, and commitments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain long-lived personal or work context for agents.

Mitigation: Use it only where persistent agent memory is intended, keep bearer tokens and other secrets out of memory, and review stored memories regularly.

Risk: Network service and LAN-sharing features can expose the memory engine beyond the local machine when configured broadly.

Mitigation: Prefer localhost, avoid --no-auth, require bearer-token configuration for MCP access, and enable LAN sharing only when needed.

Risk: Autostart features can keep the memory service running persistently.

Mitigation: Use lan enable only for deliberate persistent deployments and review service or startup settings during setup.

Risk: MCP configuration changes can affect which agents can access memory.

Mitigation: Review MCP config changes, agent identity, and authorization settings before applying them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [README](README.md)
- [User Guide](USER_GUIDE.md)
- [Protocol Reference](references/protocol.md)
- [FAQ](references/faq.md)
- [Security Review v0.8.5](docs/SECURITY-REVIEW-v0.8.5.md)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured CLI/MCP guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit local CLI commands and memory-handling instructions for agents; recall/context command output is text or Markdown.]

## Skill Version(s):

0.9.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
