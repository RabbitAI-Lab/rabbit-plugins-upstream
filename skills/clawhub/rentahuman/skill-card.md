## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, review applications, and coordinate real-world work. Use when the user needs something done in the physical world — picking up packages, attending events, photography, in-person meetings, taste-testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find people for physical-world tasks, post paid bounties, review applications, and coordinate work through RentAHuman.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public bounty listings may expose pickup identifiers or private locations, and posting can commit a hiring budget.

Mitigation: Approve the public listing, total budget, and number of hires before posting; share pickup identifiers and private locations only with accepted workers.

Risk: An API key can authorize bounty and messaging operations, and payment creates a financial commitment.

Mitigation: Use a dedicated API key with spending limits, require explicit approval before payment, and review and pin any optional MCP package before setup.

## Reference(s):

- [RentAHuman](https://rentahuman.ai)
- [RentAHuman API Reference](artifact/references/API.md)
- [ClawHub Release](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Text]

**Output Format:** [API requests and JSON results, with shell command examples and setup guidance]

**Output Parameters:** [Variable (search filters, bounty details, and conversation messages)]

**Other Properties Related to Output:** [Some operations create or manage paid real-world work and require explicit review and authorization.]

## Skill Version(s):

3.17.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
