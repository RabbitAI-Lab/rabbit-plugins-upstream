## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, start conversations, and coordinate real-world work. Use when the user needs something done in the physical world - picking up packages, attending events, photography, in-person meetings, taste-testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent find, contact, and hire people for real-world tasks such as package pickup, photography, event attendance, errands, and in-person meetings. Authenticated workflows can post bounties, message workers, manage applications, and coordinate completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate real-world workers and initiate account or payment-adjacent workflows.

Mitigation: Require explicit operator confirmation before posting, hiring, paying out, refunding, subscribing, changing webhook settings, or managing account keys.

Risk: Credentials such as RENTAHUMAN_API_KEY or x402 private keys could be exposed in logs or prompts.

Mitigation: Keep credentials in environment variables or approved secret storage, redact them from logs, and do not paste private keys into task descriptions or chat messages.

Risk: Physical-world tasks can expose sensitive locations or third-party personal details.

Mitigation: Share only the minimum location and contact details needed for the task, avoid exact home addresses unless strictly necessary, and review bounty text before publishing.

Risk: The API reference includes broader payment, wallet, webhook, subscription, and account-key functions beyond the core physical-task workflow.

Mitigation: Limit use to the requested workflow and treat non-core financial, webhook, subscription, and account-management actions as high-friction actions requiring review.

## Reference(s):

- [RentAHuman API Reference](artifact/references/API.md)
- [RentAHuman Homepage](https://rentahuman.ai)
- [ClawHub Skill Page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)
- [Publisher Profile](https://clawhub.ai/user/alexanderliteplo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JavaScript CLI usage, API request examples, and JSON response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke public RentAHuman API reads or authenticated account actions when the operator supplies credentials and confirms the action.]

## Skill Version(s):

2.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
