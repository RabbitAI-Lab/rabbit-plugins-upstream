## Description:

Helps Untappd users explore beers, breweries, venues, and activity, and post check-ins, toasts, and comments to their own accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users can ask an agent to find beers and venues, review profiles and activity, compare drinking history, and draft account posts for confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access requires an Untappd password and intercepted mobile-app credentials for an unofficial API.

Mitigation: Review this access method before installing and provide credentials only if you accept the account risk.

Risk: The local cache can retain your and friends' activity, including venues and comments.

Mitigation: Treat the cache as sensitive and delete cached data when it is no longer needed.

Risk: Posting tools can publish check-ins, toasts, and comments to your account.

Mitigation: Inspect each confirmation preview and approve only the intended action.

## Reference(s):

- [Untappd MCP on ClawHub](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured tool responses and natural-language answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supported reads default to compact responses; cached answers report freshness; account posts require confirmation.]

## Skill Version(s):

2.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
