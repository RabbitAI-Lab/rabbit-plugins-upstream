## Description: <br>
Use when an agent needs to operate RapidX through MCP or CLI for portfolio reads, market reads, order preview, order submit/replace/cancel, position management, algo orders, or explicit live trading verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liquiditytech](https://clawhub.ai/user/liquiditytech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, traders, and operations teams use this skill to have an agent read RapidX market and portfolio state, preview orders, submit authorized order, position, and algo actions, manage automation sessions, and verify resulting state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through real trading actions that may create financial loss. <br>
Mitigation: Use narrow, short-lived, low-notional sessions; require preview evidence and explicit authorization before write actions; verify final state with readback. <br>
Risk: Bulk cancel-all, close-all, or automation scopes can affect many orders or positions. <br>
Mitigation: Enable broad actions only when explicitly intended, review preview details carefully, and keep automation scope limited to authorized symbols, actions, order types, duration, and notional caps. <br>
Risk: Credential handling mistakes can expose secrets or leave the RapidX runtime unverified. <br>
Mitigation: Use approved secret mechanisms, never echo secrets, verify MCP or CLI credential materialization with self-checks, and stop trading workflows when verification is stale or failing. <br>


## Reference(s): <br>
- [RapidX Capability Overview](references/capability-overview.md) <br>
- [RapidX Skills / CLI / MCP Best Practices](references/best-practices.md) <br>
- [LTP RapidX Trading on ClawHub](https://clawhub.ai/liquiditytech/skills/ltp-rapidx-trading) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown guidance with inline MCP tool names and JSON CLI command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires observed MCP or rapidx CLI evidence for trading claims; write actions require preview, explicit authorization, and readback.] <br>

## Skill Version(s): <br>
1.0.16 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
