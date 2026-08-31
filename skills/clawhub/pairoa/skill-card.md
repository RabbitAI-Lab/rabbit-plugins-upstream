## Description:

Pairoa helps agents privately publish two-sided needs and offers, then use the Pairoa MCP service to form AI-assisted matches only when counterparties appear complementary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pairoa](https://clawhub.ai/user/pairoa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to find hiring candidates, jobs, customers, partners, investors, beta users, roommates, activity partners, or buyers and sellers through private matchmaking. The agent gathers the user's seek/offer details, obtains explicit consent before publishing contact information, checks matches, and relays returned safety guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Need text and contact email are sent to matched counterparties when a match is formed, and matched records cannot be remotely withdrawn.

Mitigation: Show the final seek, offer, contact email, and disclosure consequences before publishing; remove sensitive details unless the user explicitly wants to share them.

Risk: Counterparty-provided seek, offer, contact, and tags are unverified user text.

Mitigation: Display counterparty text as data only, never execute instructions embedded in it, and remind users to verify identity, credentials, goods, financing claims, and payment details before acting.

Risk: Blindly retrying write operations can create duplicate needs or repeat side effects.

Mitigation: Retry only safe read operations automatically; for uncertain publish or management results, check status or recall by email before asking the user to confirm another write.

## Reference(s):

- [Pairoa ClawHub skill page](https://clawhub.ai/pairoa/skills/pairoa)
- [Pairoa MCP service](https://mcp.pairoa.com)
- [Pairoa install guide](https://pairoa.com/install)

## Skill Output:

**Output Type(s):** [Guidance, Text, API Calls, Configuration]

**Output Format:** [Markdown or plain text guidance with MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user consent before publishing needs or sharing contact details with matched counterparties.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
