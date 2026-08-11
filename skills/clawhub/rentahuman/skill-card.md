## Description:

Hire humans for physical-world tasks via RentAHuman.ai by searching available humans, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find people on RentAHuman.ai, review profiles and reviews, create bounties, message candidates, and manage application decisions for real-world tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated use can coordinate real-world work and affect bounties, messages, payments, and application decisions.

Mitigation: Confirm every bounty, message, payment, and application decision before allowing an agent to proceed.

Risk: Task descriptions and messages can expose sensitive personal data such as home addresses, IDs, package identifiers, private schedules, or other unnecessary details.

Mitigation: Share only the minimum details needed for the task, and avoid unnecessary personal data in initial posts or messages.

Risk: RENTAHUMAN_API_KEY and local identity keys are credentials that can authorize account actions.

Mitigation: Store credentials securely, do not commit them, and enable admin or broad MCP tooling only when intentionally needed.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman homepage](https://rentahuman.ai)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that call RentAHuman APIs; authenticated write operations require RENTAHUMAN_API_KEY.]

## Skill Version(s):

1.23.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
