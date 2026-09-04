## Description:

Query and act on Resy restaurant reservations from a shell by using curl against api.resy.com, with fpx only for one-time token bootstrap when Resy credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Resy venues, inspect availability, book or cancel reservations, and manage favorites or Priority Notify from shell workflows without running the Resy MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can use Resy credentials or a signed-in browser session to make live booking, cancellation, favorite, and notify changes.

Mitigation: Confirm venue, date, time, party size, and action intent before running write commands; prefer confirm-gated workflows when available.

Risk: Logs or shared transcripts can expose Resy tokens, profile data, reservations, or payment-method identifiers.

Mitigation: Avoid copying tokens or account output into shared logs, and redact profile, reservation, and payment fields before sharing.

## Reference(s):

- [Resy API ready-to-run requests](artifact/references/resy-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may make live Resy account changes and may return account, reservation, payment-method, or token-adjacent data.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
