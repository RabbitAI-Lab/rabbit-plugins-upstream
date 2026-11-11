## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, review applications, and coordinate real-world work. Use when the user needs something done in the physical world — picking up packages, attending events, photography, in-person meetings, taste-testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to find people for physical-world tasks, create and manage bounties, review applications, and coordinate with applicants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags account-wide credential capabilities beyond the hiring workflow.

Mitigation: Review the API reference and executable script before installation, and limit access to RENTAHUMAN_API_KEY to workflows that need it.

Risk: ClawScan flags merchant payment capabilities beyond the hiring workflow.

Mitigation: Review payment functions before use, pin the referenced package version, and require an explicit spend cap or approval for charges.

## Reference(s):

- [RentAHuman.ai](https://rentahuman.ai)
- [RentAHuman API Reference](references/API.md)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with curl examples and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may require a RentAHuman API key for bounty, messaging, and account operations.]

## Skill Version(s):

4.8.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
