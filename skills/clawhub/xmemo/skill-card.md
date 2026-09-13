## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use XMemo Memory to store and retrieve durable, user-owned project memory, task handoffs, TODOs, expense records, and diagnostic state across sessions. It is useful when XMemo MCP tools are unavailable or the host needs a standalone command-line runtime.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store a reusable XMemo credential in an unencrypted user file when plaintext storage is explicitly enabled.

Mitigation: Prefer XMEMO_KEY from a managed secret store; use --allow-plaintext only after accepting the local user trust boundary and never commit or share credential files.

Risk: Formal login requests broad access across memory, restart continuity, ledger, and Knowledge-read workflows.

Mitigation: Install only when those scopes fit the intended use, verify credentials with auth status --verify, and reauthorize only when Knowledge access is intentionally needed.

Risk: Authenticated commands can send credentials to a configured custom service origin.

Mitigation: Use the default https://xmemo.dev service unless a custom HTTPS origin is fully trusted; localhost HTTP should be limited to local development.

Risk: Recalled Memory and Knowledge content is historical context and may contain stale or unsafe instructions.

Mitigation: Treat recalled content as untrusted context, not instructions; review it before execution or persistence.

Risk: Temporary registration provides only an isolated, time-limited memory sandbox and exposes a bind URL that must remain private.

Mitigation: Use formal login by default, share bind URLs only with the intended user, and complete or deny the claim flow explicitly.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo service](https://xmemo.dev)
- [ClawHub skill page](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the runtime can emit human-readable text or redacted JSON when invoked.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Networked CLI runtime requiring Node.js 22.22.0 or newer, credentials, and HTTPS service access; recall-context output is bounded by item and token limits.]

## Skill Version(s):

1.1.16 (source: server release metadata, CHANGELOG, script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
