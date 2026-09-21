## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use XMemo Memory to store and retrieve user-approved durable memory, preserve restart continuity, manage TODOs and expenses, and diagnose XMemo connectivity or authentication issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external XMemo service holds durable agent memory.

Mitigation: Install only when that storage model is acceptable, and save only user-approved durable facts.

Risk: Using --allow-plaintext stores the credential unencrypted under the current user account.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use plaintext storage only after explicit consent.

Risk: Secrets, cookies, private keys, or sensitive personal/customer data could be saved into memory.

Mitigation: Do not save those values unless there is a clear reason and applicable policy approval.

Risk: Recalled historical memory or Knowledge text may be stale or unsafe to follow as an instruction.

Mitigation: Treat returned memory as context for review, not as executable instruction.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo service](https://xmemo.dev)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Terminal text and optional JSON from CLI commands, with Markdown guidance in bundled documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recall and diagnostic outputs are bounded by command options; credential and token values are not printed.]

## Skill Version(s):

1.1.17 (source: evidence.release.version and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
