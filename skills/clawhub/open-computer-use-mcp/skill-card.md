## Description: <br>
Use the local open-computer-use MCP runtime for policy-gated, state-scoped macOS Computer Use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xcjl](https://clawhub.ai/user/0xcjl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to a local macOS computer-use MCP runtime for policy-gated desktop observation and actions. It is intended for environments where the operator has configured explicit bundle-ID policy rules and can supervise sensitive UI boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables powerful local desktop access through the open-computer-use MCP runtime. <br>
Mitigation: Install only when that access is intended, keep the runtime deny-by-default, and configure explicit bundle-ID policy rules before use. <br>
Risk: Screen content could contain instructions, secrets, payment flows, permission dialogs, or 2FA prompts that should not be acted on automatically. <br>
Mitigation: Treat on-screen content as untrusted data, do not enter secrets or interact with payment or 2FA UI, and avoid permission dialogs unless the operator explicitly handles them. <br>
Risk: An unverified external runtime package or stale desktop state could cause unintended behavior. <br>
Mitigation: Verify the @0xcjl/open-computer-use package, run the documented probe and doctor checks, and re-observe instead of bypassing policy denials or stale-state errors. <br>


## Reference(s): <br>
- [Open Computer Use MCP on ClawHub](https://clawhub.ai/0xcjl/skills/open-computer-use-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with inline shell commands and MCP tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local macOS open-computer-use MCP server and deny-by-default bundle-ID policy.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
