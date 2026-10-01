## Description:

Helps agents search Untappd beers, breweries, and venues, review account activity, and manage check-ins and other account interactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users can ask an agent about beers, venues, their own or accessible friends' activity, and beer history, or request check-ins and account interactions after reviewing the proposed action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an Untappd password and mobile client credentials obtained through intercepted app traffic.

Mitigation: Use only credentials you are authorized to provide, keep them out of prompts and logs, and review how they are stored before installation.

Risk: Some account-changing and deletion capabilities are not fully apparent from the top-level description.

Mitigation: Review each proposed write or deletion against the user's intent before approving it; do not enable automatic confirmation without understanding the consequences.

Risk: A local cache can retain your and friends' check-ins, comments, and venues until removed.

Mitigation: Limit access to the cache and remove stored activity when it is no longer needed.

## Reference(s):

- [Untappd MCP skill release](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may be condensed; cached activity reports freshness and completeness. Account changes require confirmation unless the server is configured otherwise.]

## Skill Version(s):

2.2.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
