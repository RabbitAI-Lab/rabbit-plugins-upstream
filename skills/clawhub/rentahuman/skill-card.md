## Description:

Helps agents find and hire people for real-world tasks through RentAHuman.ai, including posting bounties, reviewing applicants, and coordinating work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search for local workers, post paid tasks, evaluate applications, and coordinate physical-world work through RentAHuman.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posting a bounty can commit to paid real-world work without an enforced preview or confirmation step.

Mitigation: Manually review and explicitly approve the bounty, price, location, and scope before posting.

Risk: Messages, applicant decisions, and payment-related actions may have real-world or financial consequences.

Mitigation: Review each action before sending it and grant API-key access only when needed.

Risk: Listings or messages may expose private addresses, access details, schedules, financial information, or secrets.

Mitigation: Omit sensitive details from public listings and share only the minimum necessary information through appropriate channels.

## Reference(s):

- [RentAHuman API reference](references/API.md)
- [RentAHuman](https://rentahuman.ai)
- [ClawHub skill release](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include worker profiles, bounty details, and application or message responses.]

## Skill Version(s):

3.12.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
