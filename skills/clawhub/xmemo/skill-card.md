## Description: <br>
Persistent user-owned memory for agents with standalone runtime execution, including recall, search, handoff state, TODOs, expenses, and XMemo authentication diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xmemo](https://clawhub.ai/user/xmemo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to give agents durable, user-owned memory across sessions and projects. It supports remembering and recalling context, saving handoff state, managing TODOs, recording expenses, and diagnosing XMemo authentication or service issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated commands use a hosted memory service and may send credentials to a configured XMemo origin. <br>
Mitigation: Use the default XMemo service or only trusted HTTPS custom origins; run anonymous diagnostics when credentials are not needed. <br>
Risk: Plaintext local token storage may be readable by same-user local processes or backups. <br>
Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting the local storage boundary. <br>
Risk: Agents could store secrets or sensitive personal data in durable memory. <br>
Mitigation: Do not save tokens, API keys, cookies, private keys, or sensitive personal data unless explicitly authorized and policy-compatible. <br>


## Reference(s): <br>
- [XMemo Skill Operations](references/operations.md) <br>
- [XMemo Skill Troubleshooting](references/troubleshooting.md) <br>
- [XMemo service](https://xmemo.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require Node.js 20 or newer, network access to XMemo, and an authenticated credential for non-anonymous operations.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata, CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
