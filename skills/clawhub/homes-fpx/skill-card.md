## Description:

Query Homes.com through the fpx CLI and the user's signed-in browser session to search listings, resolve addresses, fetch property details, photos, and history, and read saved homes or searches when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate fpx commands and parsing recipes for Homes.com listing searches, property detail pages, address resolution, account saved pages, and bridge health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unpinned global browser-bridge CLI can introduce dependency drift or unexpected code execution.

Mitigation: Pin and verify the npm dependency before installation, and review the skill before installing it.

Risk: Using a signed-in Homes.com browser session can expose account-specific saved homes or saved searches.

Mitigation: Use a dedicated browser profile signed into only the intended Homes.com account, and avoid saved-homes or saved-searches commands unless that private account data should be read.

Risk: Examples that write response bodies under /tmp can leave listing or account data behind on shared systems.

Mitigation: Use a private mktemp directory for scratch files and clean it up after use.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub homes-fpx release page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, Node.js, and jq snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces request and extraction recipes for fpx-mediated Homes.com access; saved homes and saved searches require an explicit signed-in session.]

## Skill Version(s):

1.4.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
