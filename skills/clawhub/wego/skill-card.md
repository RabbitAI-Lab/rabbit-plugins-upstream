## Description:

Wego helps an agent use the Wego CLI to authenticate, resolve travel inputs, search and compare flights and hotels, inspect fares or room rates, answer travel reference questions, and generate checkout or share links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wego](https://clawhub.ai/user/wego)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to plan travel through Wego by resolving places and dates, comparing flight and hotel options, checking travel reference data, and continuing selected options to checkout links. It is intended for agents that can run the installed `wego` command and present concise, human-readable travel choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends installing the CLI through a remote pipe-to-shell command.

Mitigation: Require explicit user approval before installation and prefer a downloaded, versioned, checksum- or signature-verified artifact when possible.

Risk: Travel searches, preferences, and feedback may be sent to Wego's authenticated API.

Mitigation: Confirm when live searches, stored preference changes, updates, skill installation, or feedback submission will occur before taking those actions.

Risk: The skill can write user-owned Wego configuration such as currency, market, and locale.

Mitigation: Ask for the user's agreement before `wego config set` or `unset`; use one-off command flags when the user does not want stored preferences changed.

Risk: Generated checkout links hand off to Wego or providers but do not complete booking, reservation, payment, cancellation, or modification.

Mitigation: State that checkout links must be reviewed and completed by the user on the destination page, and that no booking has occurred.

Risk: The Wego visa-free lookup is not a definitive entry-requirement check.

Mitigation: Present it as Wego's inspiration list only and direct users to official destination sources for visa requirements.

## Reference(s):

- [Wego ClawHub skill page](https://clawhub.ai/wego/skills/wego)
- [Wego publisher profile](https://clawhub.ai/user/wego)
- [Wego CLI installer](https://api.wego.com/install)
- [Wego API rate limits](https://docs.wego.com/api/rate-limits/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands, JSON-derived travel results, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Wego API data; some search identifiers and checkout links expire within minutes.]

## Skill Version(s):

1.0.1 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
