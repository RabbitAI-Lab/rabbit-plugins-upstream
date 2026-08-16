## Description:

XMemo Memory gives agents persistent user-owned memory through a standalone runtime and optional MCP integration for remembering, recalling, searching memory, preserving restart continuity, managing TODOs, recording expenses, and diagnosing auth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent needs durable memory across sessions, project handoffs, TODO tracking, expense capture, or XMemo authentication diagnosis. It supports standalone Node.js execution and can defer to native XMemo MCP tools when they are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may store secrets, private customer data, or sensitive personal data in persistent memory.

Mitigation: Do not save secrets or sensitive personal/customer data unless the user explicitly asks and the memory service supports the required privacy policy.

Risk: Standalone credential setup can store a token unencrypted in the current user's XMemo directory when plaintext storage is explicitly allowed.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting the local-user trust boundary.

Risk: Authenticated commands send credentials to the configured XMemo service origin.

Mitigation: Use the default https://xmemo.dev service or trusted HTTPS origins only; plain HTTP should be limited to localhost or loopback development.

Risk: Temporary access has limited capability and lifetime, so restart continuity and other formal-account operations may fail.

Mitigation: Use formal login for the full command set, and rely on temporary registration only when a human is unavailable or explicitly declines registration.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo](https://xmemo.dev)
- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime commands can emit terminal text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands require Node.js 20 or newer, network access to the selected XMemo service origin, and an approved credential for authenticated operations.]

## Skill Version(s):

1.1.8 (source: evidence.release.version, CHANGELOG, runtime constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
