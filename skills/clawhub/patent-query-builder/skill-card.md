## Description:

Builds broad, medium, and narrow patent search queries from technical descriptions, expands synonyms, and checks hit counts against the PatentMax database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent researchers use this skill to turn a technical topic into three calibrated patent search queries, with tested hit counts and a spreadsheet-ready comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search terms and technical descriptions may expose confidential or pre-filing invention details to an external service.

Mitigation: Share only material you are comfortable sending to PatentMax/ip930.com; do not submit unpublished trade secrets or pre-filing details without authorization.

Risk: Live searches may incur API charges.

Mitigation: Review expected search volume and API charges before running queries.

Risk: API credentials, service configuration, and local cache or state can persist on shared machines.

Mitigation: Keep PATENTMAX_API_KEY and PATENTMAX_BASE_URL under your control and review ~/.patentmax files after use on shared devices.

## Reference(s):

- [PatentMax query syntax](artifact/references/query-syntax.md)
- [PatentMax query construction](artifact/references/query-construction.md)
- [PatentMax API reference](artifact/references/api-reference.md)
- [PatentMax search workflow](artifact/references/search-workflow.md)
- [ClawHub skill listing](https://clawhub.ai/ip930/skills/patent-query-builder)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Markdown response and UTF-8 CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Three query tiers with tested hit counts, top-ten relevance counts, and a recommended tier.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
