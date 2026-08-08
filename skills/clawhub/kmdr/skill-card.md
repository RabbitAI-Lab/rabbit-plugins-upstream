## Description:

Kmoe 漫画下载器。支持搜索漫画、下载漫画、管理凭证池等。当用户想要从 Kmoe 网站下载漫画、搜索漫画、管理下载账号配额时触发此 skill。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrisis58](https://clawhub.ai/user/chrisis58)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Kmoe manga, plan downloads, check quota, start background downloads, and report download progress through the kmdr CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials may be exposed if the user gives the agent a Kmoe password for login.

Mitigation: Prefer that the user runs login directly in a terminal instead of sharing the password in chat.

Risk: Downloads can consume quota or save files to an unintended destination.

Mitigation: Confirm the configured destination and available quota before starting a download.

Risk: Background downloads and stored credentials may continue or persist outside the chat session.

Mitigation: Track returned task IDs, check progress on request, and remind users that local credentials and background tasks may remain after the conversation.

Risk: The skill depends on the third-party kmdr CLI package and Kmoe account workflow.

Mitigation: Install and use the CLI only when the user trusts the package and account workflow.

## Reference(s):

- [Output Format](references/output-format.md)
- [Error Codes](references/error-codes.md)
- [Kmoe](https://kxx.moe/)
- [ClawHub Skill Page](https://clawhub.ai/chrisis58/skills/kmdr)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON or NDJSON command output interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses kmdr toolcall mode for structured command results and may report task IDs, quota estimates, and background download progress.]

## Skill Version(s):

1.0.0-a4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
