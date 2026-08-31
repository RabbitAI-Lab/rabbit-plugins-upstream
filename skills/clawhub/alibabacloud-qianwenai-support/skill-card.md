## Description:

Creates, tracks, updates, closes, and rates QianWen support tickets from chat after diagnosing common issues and requiring confirmation for state-changing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and QianWen users use this skill to manage QianWen support ticket workflows from an agent conversation. It is intended for explicit ticket operations such as creating, listing, viewing, replying to, closing, and rating support tickets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a QianWen CLI session or QIANWEN_ACCESS_TOKEN to view and modify support tickets.

Mitigation: Install only when this credential access is acceptable, verify authentication status without exposing token values, and keep credentials out of conversation output.

Risk: Creating, replying to, closing, or rating tickets changes support state.

Mitigation: Require an explicit user confirmation after showing the ticket draft, reply draft, ticket ID, or rating action before running the command.

Risk: Ticket text can accidentally include secrets or personal data.

Mitigation: Mask sensitive values such as API keys, access keys, email addresses, phone numbers, and user IDs before submitting ticket descriptions or replies.

Risk: Broader diagnostics or update commands can affect the user's local QianWen environment.

Mitigation: Run diagnostic or update commands only when the user specifically asks for them or when they are necessary to resolve the requested ticket workflow.

## Reference(s):

- [QianWen Support API Reference](artifact/references/api-reference.md)
- [Authentication Flow](artifact/references/auth-flow.md)
- [Category Selection Strategy](artifact/references/category-selection.md)
- [Error Handling Reference](artifact/references/error-handling.md)
- [Operations Guide](artifact/references/operations-guide.md)
- [RAM Policies](artifact/references/ram-policies.md)
- [Ticket Categories Reference](artifact/references/ticket-categories.md)
- [QianWen Support Portal](https://platform.qianwenai.com/home/support)
- [QianWen CLI API Endpoint](https://cli.qianwenai.com/data/v2/api.json)
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-qianwenai-support)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands and parsed ticket status details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing ticket actions require explicit user confirmation; customer service replies are relayed verbatim.]

## Skill Version(s):

0.0.1 (source: server release evidence; artifact frontmatter metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
