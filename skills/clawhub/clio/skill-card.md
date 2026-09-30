## Description:

Connects an agent to Clio Manage to retrieve legal-practice records and, with explicit approval, update records or configure automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Legal-practice staff and authorized agents use this skill to look up Clio matters, contacts, documents, tasks, and billing records, and to perform approved updates or set up related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Clio access could expose privileged client and legal-practice data.

Mitigation: Trust the Maton broker before connecting; use read-only scopes and a narrowly scoped Clio account when possible.

Risk: Write or delete requests could alter matters, contacts, or billing records.

Mitigation: Confirm each action with the user and verify the exact resource identifiers before execution.

Risk: Automations or external trigger destinations could disclose legal data or continue acting unattended.

Mitigation: Avoid third-party destinations for legal data, approve automation explicitly, and revoke unused connections, functions, and triggers promptly.

## Reference(s):

- [Clio API documentation](https://docs.developers.clio.com/api-reference/)
- [Maton](https://maton.ai)
- [Clio skill release](https://clawhub.ai/byungkyu/skills/clio)
- [Time trigger reference](references/time/triggers.md)
- [Gmail trigger reference](references/google-mail/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed writes and automation require explicit user approval.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
