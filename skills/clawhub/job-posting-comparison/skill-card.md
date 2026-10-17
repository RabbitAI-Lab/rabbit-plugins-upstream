## Description:

Compares advertised roles across job datasets, employer career boards, and Indeed while preserving posting identity, requirements, and compensation context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and career advisers use the skill to shortlist advertised roles and compare requirements, locations, and compensation on a consistent basis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search parameters and selected public URLs are sent to Crawlora, and the service requires an API key.

Mitigation: Use only if comfortable sharing those inputs with Crawlora, and keep the API key private.

Risk: The documented scraping endpoint could be used on unrelated or private pages.

Mitigation: Limit requests to public job postings or employer career pages; do not include resumes, secrets, or unrelated private data.

## Reference(s):

- [Job posting comparison endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/job-posting-comparison)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown comparison with posting ledger, requirements and compensation matrix, and follow-up questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps posting sources and observation times distinct; flags missing fields and non-comparable pay bases.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
