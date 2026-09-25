## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property detail, photos, and history, and read the signed-in user's saved homes through the user's own signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data users use this skill to make one-shot homes.com requests from an agent or shell workflow when they need listing search, address resolution, property details, saved homes, or saved searches without running the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's own authenticated homes.com browser session, and saved homes or saved searches can include private account data.

Mitigation: Run only requests the user intends, treat saved-account outputs as private data, and avoid sharing fetched account pages or extracted results.

Risk: The workflow depends on third-party @fetchproxy/cli and the Transporter extension having access to a homes.com tab.

Mitigation: Review and trust the fpx CLI and Transporter extension before pairing them with an authenticated browser session.

Risk: homes.com address resolution can return the closest result rather than a confirmed match.

Mitigation: Verify resolved candidates against the requested street address before using detail-page data.

## Reference(s):

- [homes-fpx Skill Page](https://clawhub.ai/chrischall/skills/homes-fpx)
- [homes.com request recipes](references/homes-requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON extraction snippets, jq filters, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on the fpx CLI, the Transporter browser extension, and an available homes.com browser session; saved-home and saved-search recipes require a signed-in tab.]

## Skill Version(s):

2.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
