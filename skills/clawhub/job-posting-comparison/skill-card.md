## Description:

Compare advertised job postings using Crawlora job listings, employer hiring boards, and Indeed details while preserving employer identity, location, seniority, compensation units, and offer limitations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and career advisers compare advertised roles against stated preferences, using employer and requisition evidence to assess requirements, location, and compensation without treating postings as offers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job queries, posting identifiers, and scraped public URLs are sent to Crawlora using an API key.

Mitigation: Use the key only for bounded job-comparison requests; do not send private resumes, credentials, or non-public URLs in scrape bodies.

Risk: Stored postings and incomplete provider fields can misrepresent current availability or compensation.

Mitigation: Verify employer and requisition identity, retain source dates, label missing fields unknown, and normalize salary periods before comparison.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/job-posting-comparison)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown comparison with a role ledger, requirements and compensation matrix, fit evidence, and follow-up questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves posting sources and dates; separates unknown fields from confirmed facts.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
