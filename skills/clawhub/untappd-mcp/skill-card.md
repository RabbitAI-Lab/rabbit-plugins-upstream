## Description:

Helps agents search Untappd beers, breweries, and venues, explore profiles and activity, and post confirmed check-ins, toasts, and comments to the user's account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users and their assistants can look up beers and venues, review account or friend activity, compare beers against past check-ins, and, with confirmation, post account activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires account login secrets and unofficial mobile client credentials.

Mitigation: Use only if comfortable providing these credentials; keep them private and review account access before installation.

Risk: Check-ins, toasts, and comments can change public account activity.

Mitigation: Keep confirmation enabled and review each proposed action before approving it.

Risk: A local cache can retain personal and friends' activity until removed.

Mitigation: Review cache retention and delete cached users or data when no longer needed.

## Reference(s):

- [Untappd MCP skill listing](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of Untappd results and action confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search and activity results may be incomplete when pages remain or history is unavailable.]

## Skill Version(s):

2.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
