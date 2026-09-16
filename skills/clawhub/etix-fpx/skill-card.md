## Description:

Query etix.com event-discovery data from a shell with the fpx CLI, including event, venue, performer, geolocation, and detail lookups through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Etix discovery data from scripts or shell workflows without running the etix-mcp server. It supports event and venue search, id resolution, detail extraction, and geolocation checks while keeping ticket purchasing out of scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the Transporter extension and a domain-scoped fpx browser bridge for etix.com.

Mitigation: Install only when that browser bridge is acceptable, keep the profile scoped to etix.com, and remove the fpx profile or browser pairing when no longer needed.

Risk: The setup instructions install @fetchproxy/cli from npm without a pinned version.

Mitigation: Prefer pinned npm versions and avoid elevated privileges during installation.

Risk: Etix HTML responses can still be DataDome interstitial pages even when a fetch command exits successfully.

Mitigation: Check fetched HTML for DataDome interstitial markers before parsing or using event and venue details.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell, JavaScript, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command patterns and extraction recipes for JSON, HTML, JSON-LD, microdata, and dataLayer responses.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
