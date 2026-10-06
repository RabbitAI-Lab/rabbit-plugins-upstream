## Description:

Search Untappd beer and venue information, review account activity, and manage check-ins through an Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users and their assistants can look up beers, breweries, venues, and account activity, and post check-ins, toasts, or comments with approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup requires Untappd account credentials and intercepted mobile app credentials.

Mitigation: Install only if comfortable providing these credentials; protect them and restrict access.

Risk: Write actions can post publicly or change account state.

Mitigation: Require explicit approval for posts and account changes; review each proposed action.

Risk: Local synchronization retains account and friend activity, including check-ins, comments, and venues.

Mitigation: Limit access to the local cache and remove synced user data when no longer needed.

## Reference(s):

- [Untappd MCP on ClawHub](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some results are partial until synchronization or pagination completes.]

## Skill Version(s):

2.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
