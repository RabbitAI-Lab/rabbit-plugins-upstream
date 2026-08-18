## Description:

Mail Messenger helps agents send email through SMTP, retrieve mail through documented IMAP workflows, and prepare webhook or bot notifications for common providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to draft and run email, mail-retrieval, and notification workflows while keeping credentials in environment variables or injected parameters. It is suited for sending reports, notifying users when jobs finish, and checking mail by subject, sender, or date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound email and webhook actions can send content or attachments to unintended recipients or endpoints.

Mitigation: Confirm recipients, webhook URLs, subject lines, and attachments before sending, and test with a controlled recipient first when risk is high.

Risk: Credentials, account details, message contents, or addresses could be exposed if placed in commands, logs, notes, or persistent learning records.

Mitigation: Keep credentials in environment variables or injected parameters, avoid storing sensitive details in learner notes, and remove or disable the learner when persistent learning is not needed.

Risk: Persistent self-learning records and possible skill-file changes may alter future behavior without clear limits.

Mitigation: Review learned_patterns.json and any proposed skill changes before reuse or deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/mail-messenger)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and Python usage examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local scripts for SMTP sending and persistent usage learning.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
