## Description:

Use when an agent needs to operate RapidX through MCP or CLI for portfolio reads, market reads, order preview, order submit/replace/cancel, position management, algo orders, or explicit live trading verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liquiditytech](https://clawhub.ai/user/liquiditytech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external Agent users use this skill to operate RapidX through MCP or CLI for market and portfolio reads, previewed order lifecycle actions, position and algo workflows, bounded automation, and live-trading verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can operate RapidX with trading credentials and perform real trade writes.

Mitigation: Install only when agent-operated RapidX trading is intended; use manual mode for ordinary trades and require preview evidence plus explicit authorization before writes.

Risk: Automation can submit matching order previews within a user-authorized session without another per-order confirmation.

Mitigation: Enable automation only with tight symbol, notional, order-type, action, and time limits that the user is comfortable risking.

Risk: Trading credentials or API host values could be exposed in chat, logs, or summaries.

Mitigation: Use an authorized secret mechanism for credentials and do not echo full keys.

Risk: Timeouts, asynchronous cancels, or changed business parameters can leave trade state uncertain.

Mitigation: Query current state before retrying, keep preview and submit parameters unchanged, and verify final order, position, transaction, or algo state through readback.

## Reference(s):

- [RapidX Skills / CLI / MCP Best Practices](references/best-practices.md)
- [RapidX Capability Overview](references/capability-overview.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline command examples and structured evidence expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires observed RapidX MCP or CLI evidence for portfolio, order, position, and trading claims; write actions require preview evidence and explicit user authorization.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
