## Description: <br>
Use when an agent needs to install or configure RapidX CLI/MCP access, set production LTP credentials, locate the agent workspace MCP config, review integration, discover tools, or run read-only self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liquiditytech](https://clawhub.ai/user/liquiditytech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to configure RapidX CLI or MCP access, set required LTP credentials, verify runtime readiness, and produce setup reviews before using separate trading workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill can give an agent environment configured with production RapidX credentials access to live trading actions. <br>
Mitigation: Install only in intended agent environments, prefer least-privileged or read-only credentials where possible, and require explicit preview plus confirmation before live trade, cancel, position, leverage, algo, or automation actions. <br>
Risk: Production credentials may be persisted in agent or MCP configuration. <br>
Mitigation: Use a host secret manager, chat-secret mechanism, or environment references instead of writing real keys into shared configuration, and avoid shared workspaces for production keys. <br>


## Reference(s): <br>
- [RapidX Capability Overview](references/capability-overview.md) <br>
- [RapidX Skills / CLI / MCP Best Practices](references/best-practices.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON or YAML configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include masked credential references, runtime readiness classifications, and integration review tables.] <br>

## Skill Version(s): <br>
1.0.16 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
