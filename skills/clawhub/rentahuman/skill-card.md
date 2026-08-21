## Description:

Hire humans for physical-world tasks via RentAHuman.ai, including searching available humans by skill, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use rentahuman to find, evaluate, hire, message, and pay people for physical-world tasks such as errands, event support, photography, testing, package pickup, and in-person work.

### Deployment Geography for Use:

Global, subject to RentAHuman marketplace availability and local laws.

## Known Risks and Mitigations:

Risk: The skill can initiate real-world hiring workflows and coordinate physical tasks.

Mitigation: Require explicit user confirmation before posting tasks, accepting workers, or sending task instructions, and keep instructions limited to information needed for the job.

Risk: Authenticated actions can involve payments, escrow, wallet balances, direct transfers, or payment release.

Mitigation: Require explicit user confirmation before funding, paying, releasing, transferring, withdrawing, or changing wallet controls, and verify the recipient, amount, and task status.

Risk: Messages and bounty descriptions may include personal, location, schedule, or access details.

Mitigation: Minimize sensitive data and avoid sharing home addresses, credentials, government ID data, package identifiers, schedules, or private access instructions unless strictly necessary.

Risk: The skill exposes account administration, API key management, webhook registration, and persistent local identity capabilities.

Mitigation: Keep API keys in environment variables, protect local identity files, and require explicit confirmation before creating or revoking keys, linking accounts, or registering webhooks.

## Reference(s):

- [RentAHuman homepage](https://rentahuman.ai)
- [RentAHuman MCP API Reference](references/API.md)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and CLI/API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated write, payment, account, webhook, and messaging actions require RENTAHUMAN_API_KEY.]

## Skill Version(s):

1.27.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
