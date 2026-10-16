## Description:

Find developers through Crawlora public GitHub user datasets and verify relevant repository and contribution evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, hiring teams, and open-source collaborators use this skill to find developers and build role-specific shortlists grounded in public repository and contribution evidence, without initiating outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Crawlora API key is required to query public GitHub-derived profiles.

Mitigation: Protect the key, keep queries narrow, and set a credit budget.

Risk: Public profiles, contact details, and activity signals may be stale or misread as verified hiring qualifications.

Mitigation: Preserve crawl and observation dates, verify linked work, and treat availability and professional fit as unconfirmed.

Risk: Discovery results could be misused for bulk outreach or private-data enrichment.

Mitigation: Limit use to scoped public professional evidence; do not conduct bulk outreach or enrich private information.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/developer-talent-discovery)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown shortlist with profile and work-evidence links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source dates, declared availability fields, technical interpretation, and unknowns requiring follow-up.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
