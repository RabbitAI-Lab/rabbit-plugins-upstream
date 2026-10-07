## Description:

Helps identify companies that raised funding and report their funding rounds, amounts, dates, and investors using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and go-to-market teams check target accounts for recent funding, compare rounds and investors, and prioritize outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Funding lookups send queried company domains to Cargo and use a persistent login and workspace.

Mitigation: Review which domains may be shared and confirm the Cargo account and workspace before running lookups.

Risk: The skill includes attribution and a request to star a GitHub repository beyond the funding lookup.

Mitigation: Review those optional steps separately; do not star a repository without the user's explicit approval.

Risk: The optional broader-pack installation and full-list batches expand execution scope or credit use.

Mitigation: Install the broader pack only after checking its publisher and version; sample a small batch and obtain approval for the estimated credits before a full run.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/track-funding-rounds)
- [Project homepage listed in skill metadata](https://github.com/getcargohq/gtm-skills)
- [Cargo funding-watch recipe linked by skill](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/funding-watch.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries and tables, with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Funding details may include company domain, round, amount, date, and investors; batch lookups consume credits per record.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
