## Description:

Analyzes restaurant brand competitor-network changes, priority areas, and market actions from Amap/Gaode address text using 店店通 published store snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External business analysts, market teams, and sales teams use this skill to analyze published restaurant brand store snapshots, compare competitor expansion or contraction, screen nearby stores or candidate sites, and produce action-oriented market intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party 店店通 API service and requires a user-provided DDT_API_KEY.

Mitigation: Confirm comfort with the third-party service before installation and keep DDT_API_KEY only in local environment variables.

Risk: Restaurant conclusions are limited to 店店通 published snapshots and may not represent official brand disclosures or real-time conditions.

Mitigation: Report the coverage period and data basis in outputs, avoid filling gaps with model memory or web claims, and stop business conclusions when required capabilities or published data are unavailable.

Risk: The skill is not an official Amap/Gaode product and has no documented Amap/Gaode partnership, authorization, or data-source relationship.

Mitigation: Describe Amap/Gaode text only as user-provided address input and attribute store-network conclusions to 店店通 snapshots.

Risk: Preview endpoints can be truncated and are not intended for full store-directory export.

Mitigation: Use aggregate endpoints first, limit detail queries to explicit user requests, and narrow filters instead of auto-paginating or assembling full store lists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-amap-restaurant-competitor)
- [店店通 DDT Claw homepage](https://gotoshop-ai.com/ddtclaw/)
- [店店通 DDT Claw API key setup](https://gotoshop-ai.com/ddtclaw/open)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise business analysis and optional bash/curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local DDT_API_KEY; outputs conclusions, key metrics, coverage period, data caveats, limited requested details, and uncovered items.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
