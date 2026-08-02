## Description: <br>
Persistent user-owned memory for agents with standalone runtime execution. Use when an agent should remember, recall, search memory, save or restore handoff state, manage TODOs, record expenses, diagnose XMemo auth, or operate XMemo even when MCP tools are not configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xmemo](https://clawhub.ai/user/xmemo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to give agents durable, account-backed memory across sessions, including recall, search, handoff state, TODOs, expenses, and XMemo authentication diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaintext local token storage can expose XMemo bearer credentials to same-user processes or accidental file sharing. <br>
Mitigation: Prefer XMEMO_KEY or an OS/managed secret store; use --allow-plaintext only with informed consent and treat ~/.xmemo/skill-credentials.json as a sensitive bearer-token file. <br>


## Reference(s): <br>
- [XMemo Skill Operations](artifact/references/operations.md) <br>
- [XMemo Skill Troubleshooting](artifact/references/troubleshooting.md) <br>
- [XMemo service](https://xmemo.dev) <br>
- [ClawHub skill page](https://clawhub.ai/xmemo/skills/xmemo) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Standalone Node.js runtime can print compact human-readable results or redacted JSON with --json.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
