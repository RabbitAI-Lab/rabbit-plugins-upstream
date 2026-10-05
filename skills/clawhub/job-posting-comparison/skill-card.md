## Description:

Compare advertised job postings using Crawlora job datasets, employer career boards, and Indeed details while preserving role identity, requirements, location, and compensation context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and career advisers use this skill to shortlist and compare advertised roles against a candidate's requirements, with evidence for fit, compensation, and open questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job queries, employer identifiers, public posting URLs, and the Crawlora API key are shared with Crawlora when using its service.

Mitigation: Use the service only if this sharing is acceptable; keep the key private and do not send resumes, private profiles, or account information unless intentionally authorized.

Risk: Indexed postings can lag live career boards, and missing details or salary units can lead to misleading comparisons.

Mitigation: Verify roles against the employer's official posting, preserve source dates and unknown fields, and compare compensation only on a stated, consistent basis.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/job-posting-comparison)
- [Crawlora job endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown comparison matrix and short narrative]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes employer and requisition identifiers, source links and dates, fit evidence, compensation assumptions, and unanswered questions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
