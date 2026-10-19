## Description:

Analyzes recently granted Chinese invention patents in a technical field to estimate filing-to-grant times and support planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent applicants, IP teams, and advisors use recent Chinese invention-patent grants to estimate typical approval timelines for filing, project, and funding plans.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Patent queries and technical descriptions are sent to an external PatentMax service.

Mitigation: Avoid confidential unpublished inventions unless external processing is acceptable.

Risk: API credentials are used with an external service, and changing its endpoint could expose them to an untrusted host.

Mitigation: Use the intended PatentMax endpoint; set PATENTMAX_BASE_URL only in a trusted test environment.

Risk: Broader patent searches or analyses may incur charges beyond the free allowance.

Mitigation: Review paid-call behavior and expected costs before running broader searches.

Risk: Historical granted-patent samples exclude rejected or withdrawn applications and may not predict an individual outcome.

Mitigation: Present results as historical estimates and explain that review timelines can vary.

## Reference(s):

- [PatentMax API reference](references/api-reference.md)
- [Patent search workflow](references/search-workflow.md)
- [Patent query syntax](references/query-syntax.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Markdown response and UTF-8 CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CSV includes grant-time statistics and the underlying patent sample.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
