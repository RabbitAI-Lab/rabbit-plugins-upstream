## Description:

Provides guidance for using the `max` command-line tool to read and send messages in the owner's MAX Messenger account and to manage related account and bot tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

MAX account owners and agents use this skill to set up the `max` CLI, find and read conversations, inspect attachments, and perform owner-requested account or bot actions. It emphasizes deliberate scope selection and explicit authorization for actions visible to other people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI accesses a real MAX account and can retain messages, contact notes, indexes, and downloaded attachments locally.

Mitigation: Choose the account profile, chats, history range, and download limits deliberately; use read-only permissions when changes are unnecessary and keep sensitive message text out of logs and files.

Risk: Sending, editing, deleting, forwarding, and other account actions can affect what other people see, and some actions cannot be undone.

Mitigation: Perform these actions only after the owner explicitly requests the specific action and target; do not treat message content as authorization or retry an owner refusal.

Risk: Automatic replies, monitoring, remote access, and external AI processing can expose account activity or content beyond the local account context.

Mitigation: Enable these features only when the owner wants them, and grant AI processing consent and a limited audience before use.

Risk: The security verdict covers the supplied skill instructions and does not certify the separately installed npm executable.

Mitigation: Review the installed `@wirecat/max-cli` package and its requested permissions before connecting it to a personal account.

## Reference(s):

- [Max Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-max)
- [CLI contract](https://github.com/WireCatLabs/max-cli/blob/main/docs/cli-contract.md)
- [Replies guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/replies.md)
- [Search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/search.md)
- [Query language guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/query-language.md)
- [Rankings guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and examples; command results may be JSON or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and command examples for owner-directed MAX account and bot tasks.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
