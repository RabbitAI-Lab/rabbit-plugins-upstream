## Description:

Helps an agent manage Shuning OA work records and reimbursement requests, including submitting, updating, querying time entries and checking approval progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ithou](https://clawhub.ai/user/ithou)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or their assisting agents use this skill to interact with a configured Shuning OA system for work-time records, reimbursement status checks, and approval-progress queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles saved OA credentials and short-lived OA tokens.

Mitigation: Use encrypted credentials with OA_ENC_KEY, avoid plaintext credential files, restrict credential and token files to the current user, and do not expose secrets in logs or responses.

Risk: The skill can submit, update, or delete company work records from natural-language requests.

Mitigation: Require explicit user confirmation before submit, update, or delete operations and review the target date, project, and description before execution.

Risk: The skill calls a configured OA base URL and depends on a local Python runtime.

Mitigation: Install only for the intended OA system and keep the configured base URL and Python virtual environment under user control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ithou/skills/sn-work-record)
- [Publisher profile](https://clawhub.ai/user/ithou)
- [Shuning OA API reference](references/api.md)
- [Hermes credential storage](references/hermes-credential-storage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include OA record summaries or command invocations; sensitive credentials and tokens should not be displayed.]

## Skill Version(s):

1.13.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
