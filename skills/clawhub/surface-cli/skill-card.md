## Description:

Use the Surface mail CLI to read and act on Gmail, Outlook, and generic IMAP/SMTP mail through one JSON-first contract.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vishalj99](https://clawhub.ai/user/vishalj99)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to work with mail accounts through Surface CLI: listing accounts, checking authentication, searching and reading mail, managing attachments, drafting or sending messages, and running mailbox actions with stable message and thread references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to read or act on email accounts, including send-like and mailbox mutation operations.

Mitigation: Respect the local Surface write-safety configuration, prefer drafts for compose tasks, and require clear user intent before sending mail or changing read/archive state.

Risk: Mailbox credentials, provider tokens, Outlook cookies, and email content are sensitive.

Mitigation: Avoid asking users to paste mailbox passwords into chat, prefer password environment/file/command options, and confirm the privacy tradeoff before enabling external summarization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vishalj99/skills/surface-cli)
- [Surface CLI homepage](https://github.com/VishalJ99/surface-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Surface CLI commands emit machine-readable JSON that agents should parse rather than scrape from terminal text.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
