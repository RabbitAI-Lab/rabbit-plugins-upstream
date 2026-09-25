## Description:

Squarespace Commerce API integration with managed OAuth for managing products, inventory, orders, customer profiles, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce operators use this skill to manage Squarespace Commerce store data through Maton CLI or HTTP gateway workflows, including inventory, orders, products, profiles, transactions, and user-approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or change Squarespace store, customer, order, and transaction data through the connected account.

Mitigation: Prefer OAuth, connect only the needed account and scopes, specify the intended connection, and confirm every write payload and target before execution.

Risk: API key fallback uses a long-lived credential that may leak through process environments, logs, shell history, or pasted output.

Mitigation: Use OAuth when possible; if a key is unavoidable, keep it scoped to api.maton.ai, avoid command-line exposure, and rotate it if it is printed, committed, or pasted.

Risk: Functions, triggers, and destinations can create persistent automation or standing data forwarding.

Mitigation: Create automation only after explicit approval of scope, destination host, payload fields, frequency, and network policy; remove functions, triggers, and destinations when no longer needed.

Risk: Profiles, transactions, order records, and trigger payloads may contain personal, financial, or confidential business data.

Mitigation: Read and disclose only the fields needed for the task, avoid logging raw responses, and do not copy data to other apps or destinations without specific user approval.

## Reference(s):

- [ClawHub Squarespace Skill](https://clawhub.ai/byungkyu/skills/squarespace)
- [Maton Homepage](https://maton.ai)
- [Squarespace Commerce APIs Overview](https://developers.squarespace.com/commerce-apis/overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a Maton account; normal operations should prefer OAuth and user-approved write or automation actions.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
