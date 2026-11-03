## Description:

Read a Juggle (whyjuggle.com) babysitting/petsitting FAMILY account from a shell with curl + jq, no MCP server needed. Covers your sits/jobs and who applied, one booking in detail, sitter search, favorites, sitter profiles and reviews, your message conversations, the payments summary (rates, cards by brand/last 4, promo credit, transactions in dollars), and the public city and rate list. Use it when someone asks about Juggle, whyjuggle, their babysitter or petsitter bookings, sitter applicants, or messages with a sitter, and the juggle-mcp tools aren't available, or when a script needs the data. Read-only: posting a sit, accepting or declining a sitter, cancelling, messaging, favoriting and reviewing are confirm-gated tools in juggle-mcp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Families and their assistants use this skill to review Juggle bookings, sitter applicants and profiles, conversations, payment summaries, and public city rates from a shell. Developers can consume its JSON results in scripts; the skill's commands are read-only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command results and the saved session can contain sensitive family, child, address, message, and payment information.

Mitigation: Protect the session file and restrict access to saved or shared command output containing personal information.

Risk: An untrusted custom service URL may expose sign-in credentials or account requests.

Mitigation: Use the default HTTPS service address; use URL overrides only with a trusted local test service.

Risk: The API reference and live service behavior are not verified by the release evidence.

Mitigation: Check returned data against the current service before relying on it for consequential decisions.

## Reference(s):

- [Juggle MCP ClawHub release](https://clawhub.ai/chrischall/skills/juggle-mcp)
- [Juggle service](https://whyjuggle.com)

## Skill Output:

**Output Type(s):** [JSON data, Shell command results]

**Output Format:** [JSON on stdout, with shell usage guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account-specific data depends on the signed-in Juggle family account; public location data does not require sign-in.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
