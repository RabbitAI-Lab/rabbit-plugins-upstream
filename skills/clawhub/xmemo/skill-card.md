## Description: <br>
XMemo gives agents persistent, user-owned memory with standalone runtime support for recall, search, handoff state, TODOs, expenses, and authentication diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xmemo](https://clawhub.ai/user/xmemo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use XMemo to preserve useful project memory across sessions, retrieve prior decisions, manage handoff state, track TODOs and expenses, and diagnose XMemo authentication or service access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends memory, TODO, expense, and diagnostic requests to the hosted XMemo service. <br>
Mitigation: Install and use it only when hosted XMemo service use is acceptable for the data being stored or retrieved. <br>
Risk: Local credential storage is plaintext when --allow-plaintext is used. <br>
Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only on a trusted machine within the user's local account boundary. <br>
Risk: Temporary registration creates a limited sandbox and exposes a bind URL that can connect the sandbox to a user account. <br>
Mitigation: Use temporary registration only for unattended or explicitly declined formal login flows, show the bind URL only to the intended user, and complete claim confirmation after the user claims it. <br>
Risk: Stored memory may contain inappropriate secrets or sensitive data if the agent saves too broadly. <br>
Mitigation: Do not save secrets, tokens, private keys, cookies, session IDs, or sensitive personal/customer data unless the user explicitly asks and the service's privacy posture supports it. <br>


## Reference(s): <br>
- [XMemo Skill Page](https://clawhub.ai/xmemo/skills/xmemo) <br>
- [XMemo Publisher Profile](https://clawhub.ai/user/xmemo) <br>
- [XMemo Service](https://xmemo.dev) <br>
- [Operations Reference](artifact/references/operations.md) <br>
- [Troubleshooting Reference](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Memory recall and search can be compacted for terminal display; commands can emit JSON with --json.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and bundled script constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
