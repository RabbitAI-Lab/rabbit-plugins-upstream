## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, review applications, and coordinate real-world work. Use when the user needs something done in the physical world — picking up packages, attending events, photography, in-person meetings, taste-testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT

## Use Case:

AI agents use this skill to find people for in-person tasks, review profiles and applications, post paid bounties, and coordinate the work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bounty posts may expose addresses, package identifiers, or other sensitive details.

Mitigation: Review and remove sensitive details before posting a bounty.

Risk: Authenticated operations involve account and payment capabilities.

Mitigation: Review the access needed before installing and use authenticated actions only for approved tasks.

Risk: Security review of the executable script was partial, so its behavior is not fully assessed.

Mitigation: Inspect the current script before enabling authenticated operations.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman](https://rentahuman.ai)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON requests, and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browsing is unauthenticated; posting bounties, messaging, and account management require an API key.]

## Skill Version(s):

4.9.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
