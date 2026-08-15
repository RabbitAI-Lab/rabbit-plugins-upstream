## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, start conversations, and coordinate real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find people for physical-world tasks, post bounties, start conversations, and coordinate task completion through RentAHuman.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated use may grant task-posting, messaging, account, payment, or webhook authority through RENTAHUMAN_API_KEY.

Mitigation: Install only for accounts where those actions are acceptable, review paid or account-changing actions before execution, and rotate or revoke keys that are no longer needed.

Risk: Bounties and messages can expose sensitive task details or third-party personal information.

Mitigation: Avoid secrets, unnecessary addresses, package identifiers, government ID details, payment details, and other sensitive personal information in prompts, bounties, or messages.

Risk: The CLI creates a persistent local signing identity in ~/.rentahuman-identities.

Mitigation: Treat the identity directory as credential material, restrict filesystem access, and remove unused identities when they are no longer needed.

## Reference(s):

- [RentAHuman homepage](https://rentahuman.ai)
- [RentAHuman MCP API Reference](references/API.md)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled CLI prints JSON responses for RentAHuman API operations.]

## Skill Version(s):

1.26.0 (source: server release metadata and references/API.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
