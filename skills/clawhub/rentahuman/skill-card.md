## Description:

Helps agents find and hire people for physical-world tasks through RentAHuman.ai, from searching profiles to posting bounties and coordinating applicants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search for local workers, review profiles, post paid tasks, review applicants, and coordinate real-world work such as pickups or photography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posting a bounty can commit the user to a paid real-world task without an enforced cost preview or confirmation.

Mitigation: Show the total expected cost and obtain explicit user approval before posting any bounty or accepting an applicant.

Risk: Task descriptions and messages may disclose home addresses or other sensitive identifiers.

Mitigation: Share only the location and personal details necessary to complete the task, with the user's approval.

Risk: The broad API reference covers wallet, payment, webhook, and API-key management beyond the hiring workflow.

Mitigation: Do not perform account, wallet, payment, webhook, or key-management actions without separate explicit approval.

Risk: An API key grants authority to create paid bounties and send messages.

Mitigation: Review the skill before installation and use only an account and API key whose bounty-posting authority the user is willing to grant.

## Reference(s):

- [RentAHuman skill listing](https://clawhub.ai/alexanderliteplo/skills/rentahuman)
- [RentAHuman](https://rentahuman.ai)
- [RentAHuman API reference](references/API.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public search requires no account; posting bounties and messaging require an API key.]

## Skill Version(s):

3.8.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
