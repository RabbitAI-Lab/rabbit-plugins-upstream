## Description:

XMemo Memory gives agents persistent cloud memory to recall project context, track tasks and expenses, and resume work across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use XMemo to preserve and retrieve project decisions, preferences, task state, TODOs, and expense records across sessions and tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-run sign-in can store a token unencrypted in the user's home directory.

Mitigation: Prefer XMEMO_KEY or a managed secret store; explain local token storage before choosing --allow-plaintext.

Risk: Stored memories, TODOs, ledger entries, and restart context are sent to the XMemo cloud service.

Mitigation: Keep secrets and sensitive personal data out of saved records and recall queries; review cloud storage before use.

Risk: Broad account access can change or delete records and add financial transactions.

Mitigation: Confirm ledger writes and deletions explicitly and use only the credential scopes needed for the task.

Risk: Custom service origins receive credentials, and profile setup can modify project instruction files.

Mitigation: Confirm custom origins and changes to agent instruction files before applying them.

## Reference(s):

- [XMemo Memory ClawHub release](https://clawhub.ai/xmemo/skills/xmemo)
- [Authentication setup](artifact/references/auth-setup.md)
- [Memory operations](artifact/references/memory-operations.md)
- [Ledger operations](artifact/references/ledger-operations.md)
- [Runtime operations](artifact/references/runtime-operations.md)
- [Agent profile and instruction files](artifact/references/agent-profile.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline commands and structured command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall, task continuity, TODO tracking, ledger entries, and account diagnostics require appropriate credentials and scopes.]

## Skill Version(s):

1.1.39 (source: ClawHub release metadata and artifact/CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
