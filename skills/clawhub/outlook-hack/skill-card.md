## Description:

TinkerClaw Outlook lets agents read and search Outlook mail, inspect attachments, and create or edit drafts without sending messages, using a short-lived Microsoft Graph access token supplied on stdin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers can inspect Outlook mailbox content, download attachments, and prepare draft messages for manual review without granting the skill any send capability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Microsoft Graph access token with mail scopes can expose mailbox content during a run.

Mitigation: Use only short-lived tokens with the minimum mail scopes needed for the command, supply them on stdin, and avoid storing or logging token values.

Risk: Bulk mailbox exports and downloaded attachments can leave sensitive plaintext on disk.

Mitigation: Use bulk export only with explicit consent, keep exported files in private directories, and delete exports or attachments when no longer needed.

Risk: Generated Markdown reports may contain unescaped email content that rich renderers could interpret.

Mitigation: Open generated reports cautiously and treat them as sensitive mailbox-derived content.

Risk: Draft creation or patching can change unsent Outlook messages.

Mitigation: Review every draft manually in Outlook before sending; the skill does not provide send, reply, or forward operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/outlook-hack)
- [ClawHub publisher profile](https://clawhub.ai/user/globalcaos)
- [Microsoft Graph service boundary](https://graph.microsoft.com/v1.0)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, guidance]

**Output Format:** [Console text, Markdown summaries, JSONL mailbox exports, and downloaded files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional mailbox exports and downloaded attachments are plaintext local files; draft changes require manual review in Outlook before sending.]

## Skill Version(s):

3.4.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
