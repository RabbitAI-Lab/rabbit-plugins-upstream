## Description:

Hire humans for physical-world tasks through RentAHuman.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search for local workers, post paid bounties for physical tasks, review applications, and coordinate work through messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can post paid public bounties or use broader account and payment capabilities without sufficient guardrails.

Mitigation: Preview costs and require explicit user approval before posting or funding bounties, accepting workers, messaging people, or releasing money.

Risk: Physical-world tasks and conversations can expose sensitive personal details.

Mitigation: Avoid sharing home addresses, IDs, package numbers, access codes, or sensitive schedules unless necessary.

Risk: Giving an agent an API key grants it access to paid bounties and real-world coordination.

Mitigation: Review the skill before installation and only use an API key whose permitted actions you understand and accept.

## Reference(s):

- [RentAHuman website](https://rentahuman.ai)
- [RentAHuman API reference](artifact/references/API.md)
- [ClawHub skill release](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and task coordination guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated actions require a RentAHuman API key; posting bounties can incur costs.]

## Skill Version(s):

3.14.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
