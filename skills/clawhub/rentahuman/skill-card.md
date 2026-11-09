## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, review applications, and coordinate real-world work. Use when the user needs something done in the physical world — picking up packages, attending events, photography, in-person meetings, taste-testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to find people for physical-world tasks, post paid bounties, review applications, and coordinate work through RentAHuman.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The posting shortcut skips the approval workflow described in the reference.

Mitigation: Follow the documented applicant review and acceptance steps; review the final listing and total cost, and require explicit authorization for hiring and payments.

Risk: Posting shortcuts can place sensitive details in browsable task listings.

Mitigation: Keep addresses, package identifiers, and access details in private worker instructions.

Risk: Hosted API enforcement and the optional MCP implementation remain unverified.

Mitigation: Use a dedicated API key and review the exact package version before enabling the optional MCP server.

## Reference(s):

- [RentAHuman API Reference](artifact/references/API.md)
- [RentAHuman](https://rentahuman.ai)
- [ClawHub Skill Release](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browsing is unauthenticated; posting and other write operations require RENTAHUMAN_API_KEY.]

## Skill Version(s):

4.7.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
