## Description:

Finds inventors active in a technology area using public patent records and prepares a talent shortlist for hiring, expert search, or partnerships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, researchers, and business development teams use public patent inventor and applicant records to identify potential technical experts and collaborators in a selected field.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms may disclose confidential inventions or trade secrets to PatentMax.

Mitigation: Do not submit sensitive searches unless the user approves sharing them with PatentMax.

Risk: API credentials and queries may be sent to a configurable external service.

Mitigation: Check that PATENTMAX_BASE_URL is unset or points to a trusted service before use; protect paid credentials.

Risk: Trial keys and task caches may remain in local ~/.patentmax storage.

Mitigation: Review and remove locally stored credentials and caches when they are no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-talent-finder)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax search workflow](artifact/references/search-workflow.md)
- [PatentMax query syntax](artifact/references/query-syntax.md)

## Skill Output:

**Output Type(s):** [CSV file, Text summary]

**Output Format:** [UTF-8 CSV and conversational Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventor names, patent applicants, counts, recent filing dates, representative patents, and source attribution; no contact details.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
