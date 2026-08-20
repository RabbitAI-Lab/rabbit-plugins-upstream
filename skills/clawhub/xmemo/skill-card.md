## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use XMemo Memory to preserve durable project context, recall prior decisions, manage handoffs, track TODOs and expenses, and diagnose XMemo connectivity when native MCP tools are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The standalone runtime can store an XMemo token in a local plaintext user file when explicitly allowed.

Mitigation: Prefer XMEMO_KEY or a managed secret store. Use --allow-plaintext only after accepting the local trust boundary, and do not back up, share, or commit the credential file.

Risk: Saved memories, restart state, TODOs, or expenses may contain sensitive context if the user asks the agent to store it.

Mitigation: Do not save secrets, tokens, private keys, cookies, or sensitive personal or customer data unless the user explicitly intends that storage and the service policy permits it.

Risk: Authenticated commands send credentials to the configured XMemo service origin.

Mitigation: Use the default XMemo service or only trusted HTTPS custom origins; plain HTTP should be limited to localhost or loopback development.

Risk: Temporary access is limited and uses a bind URL that could be misused if published.

Mitigation: Use formal login by default, share temporary bind URLs only with the intended user, and complete or deny the claim flow promptly.

## Reference(s):

- [XMemo Skill Operations](artifact/references/operations.md)
- [XMemo Skill Troubleshooting](artifact/references/troubleshooting.md)
- [XMemo Service](https://xmemo.dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime commands can also return text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands require Node.js 20 or newer, network access to XMemo, and a valid credential for authenticated operations.]

## Skill Version(s):

1.1.11 (source: server release metadata, CHANGELOG, and bundled runtime)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
