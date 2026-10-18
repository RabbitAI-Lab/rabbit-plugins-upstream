## Description:

Research public Resy and OpenTable restaurant listings and time-specific availability to prepare dated dining shortlists and comparisons without booking or ordering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Diners and dining researchers use this skill to compare restaurant options and observed reservation availability for a specified location, local time, and party size. It produces a dated shortlist, not a reservation or ticket purchase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant queries pass through Crawlora and require a Crawlora API key.

Mitigation: Use only if comfortable with Crawlora as an intermediary; keep the API key in a protected environment variable and do not include it in shared outputs.

Risk: Displayed availability may change and does not guarantee a table or ticket.

Mitigation: Label results as dated snapshots, include the retrieval time, and verify availability with the provider before making plans.

## Reference(s):

- [Skill listing on ClawHub](https://clawhub.ai/crawlora-org/skills/dining-demand-research)
- [Restaurant research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text or Markdown comparison and shortlist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local date and time, party size, provider, source, and retrieval timestamp for observed availability; distinguishes ordinary reservations from events.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
