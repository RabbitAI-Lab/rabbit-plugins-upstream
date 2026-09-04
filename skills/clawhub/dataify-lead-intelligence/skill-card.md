## Description:

Discover and rank companies that match an ideal customer profile using public company, hiring, and market evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and operations teams use this skill to discover, qualify, and rank company prospects against an ideal customer profile using public evidence. It is intended for company-level account research, prospect lists, territory planning, and verification-ready lead qualification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Dataify API token and may consume account credits during company research.

Mitigation: Use the environment variable token flow, verify only token presence, and use dry-run or bounded scope when cost or volume is unclear.

Risk: Lead qualification could include unsupported claims or private personal contact enrichment if results are not constrained to explicit public company evidence.

Mitigation: Score only from cited public evidence, report missing fields and disqualifiers, and avoid private personal emails, phone numbers, or invented company attributes.

## Reference(s):

- [Dataify Lead Intelligence ClawHub page](https://clawhub.ai/dataify-server/skills/dataify-lead-intelligence)
- [Dataify account setup](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with company prospect lists, evidence summaries, scores, missing fields, disqualifiers, and verification queues]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke a Dataify API-backed workflow using DATAIFY_API_TOKEN and public company sources.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
