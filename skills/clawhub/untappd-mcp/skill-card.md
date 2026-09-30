## Description:

Search Untappd beers, breweries, and venues; read account activity; and post check-ins, toasts, and comments with the user's account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users and their assistants can explore beer listings and account activity, check beer history, and publish check-ins or interactions after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untappd login and reverse-engineered mobile app credentials may be exposed.

Mitigation: Store credentials in isolated environment variables or a secrets manager and avoid logging them.

Risk: Check-ins, toasts, and comments affect the user's public account.

Mitigation: Review the action preview and obtain user approval before posting.

Risk: The local cache can retain private or friend activity.

Mitigation: Protect cache access and periodically delete cached activity that is no longer needed.

## Reference(s):

- [Untappd MCP ClawHub release](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Markdown prose and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may be partial or cached; publishing actions require confirmation.]

## Skill Version(s):

2.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
