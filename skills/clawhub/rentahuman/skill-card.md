## Description:

Helps agents find people and coordinate paid physical-world tasks through RentAHuman.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search for local workers, post paid tasks, review applications, and coordinate work through bounty conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with an API key can post paid tasks or make applicant decisions without adequate approval.

Mitigation: Require a person to review and approve each bounty, amount, location, schedule, and applicant decision before submission.

Risk: Messages and task descriptions can disclose private addresses, account or package identifiers, and contact details to real people.

Mitigation: Review messages before sending and share only the minimum information needed to complete the task.

## Reference(s):

- [RentAHuman API reference](references/API.md)
- [RentAHuman website](https://rentahuman.ai)
- [ClawHub skill release](https://clawhub.ai/alexanderliteplo/skills/rentahuman)
- [RentAHuman API key setup](https://rentahuman.ai/account/api-keys)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance and shell commands; API responses in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated actions can post paid bounties, manage applicants, and send messages.]

## Skill Version(s):

3.10.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
