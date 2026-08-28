## Description:

Query homes.com through the fpx CLI from a signed-in browser tab to search listings, resolve street addresses, fetch property details, photos, history, nearby listings, and saved homes or searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate fpx setup guidance, shell commands, Node.js extractors, and jq filters for homes.com listing search, address resolution, property lookup, history, nearby listings, and saved homes or searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and saved searches may expose private account data from the signed-in homes.com session.

Mitigation: Confirm the browser tab is signed into the intended account and avoid saving or sharing fetched HTML or extracted results unless needed.

Risk: Requests are routed through a paired browser session, so a stale, wrong, or untrusted session can produce misleading or unintended account-scoped results.

Mitigation: Run the fpx health check, open the intended homes.com tab, clear any sign-in or WAF challenge state, and retry before relying on results.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, Node.js snippets, jq filters, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference signed-in browser session state and saved homes or saved searches when the user requests account-gated homes.com pages.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
