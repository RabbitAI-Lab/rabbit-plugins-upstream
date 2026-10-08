## Description:

Helps users find hiking trails and view trail details, reviews, weather, and their AllTrails account activity through an unofficial read-only integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and other AllTrails users can find trails, check details and reviews, export routes, and look up their saved lists or completed hikes when signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in browser session can expose saved lists, completed trails, profile, and activity without clear per-use confirmation.

Mitigation: Invoke only for explicit AllTrails requests and confirm before retrieving account-linked data.

Risk: The unofficial integration relies on an internal AllTrails API and browser bridge that may stop working or conflict with AllTrails' terms.

Mitigation: Review the integration and applicable terms before installing or using it; do not rely on it for critical trail decisions.

## Reference(s):

- [AllTrails skill release](https://clawhub.ai/chrischall/skills/alltrails)
- [AllTrails MCP package](https://www.npmjs.com/package/alltrails-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, GPX data]

**Output Format:** [Text summaries and GPX 1.1 XML for trail route exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; account data requires a signed-in AllTrails session.]

## Skill Version(s):

3.1.7 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
