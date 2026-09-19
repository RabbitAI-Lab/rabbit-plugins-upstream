## Description:

Compare advertised hiring demand across roles, skills, locations, and seniority using Crawlora's jobs dataset. Use for labor-market snapshots, employer concentration, remote-work comparisons, and salary analyses with explicit coverage and compensation-unit controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to compare observed job-posting demand across roles, skills, employers, locations, seniority, remote-work status, and compensation fields. It is intended for bounded, user-directed labor-market snapshots with explicit coverage limits, denominators, and interpretation cautions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's Crawlora API key and job-search query parameters to Crawlora.

Mitigation: Install and run it only when that external API use is acceptable; keep the API key in the environment and use bounded, user-directed requests.

Risk: Observed job postings can be mistaken for confirmed hires, full labor-market coverage, or ongoing monitoring.

Mitigation: Report results as a snapshot of observed postings, state coverage and denominators, and avoid trend claims without comparable dated snapshots.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/hiring-demand-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands, structured counts, cited posting examples, and limitations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON snippets from Crawlora API responses when useful.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
