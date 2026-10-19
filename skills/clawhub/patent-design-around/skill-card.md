## Description:

Breaks a patent's independent claim into features, proposes design-around alternatives, checks related patents, and produces a preliminary ideas table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams and patent researchers use this skill to compare a proposed design with a specified patent's independent claim, explore alternatives, and check those alternatives against patent search results. Its suggestions are preliminary and require professional review before implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent numbers, search queries, and technical product descriptions may be sent to the external PatentMax service.

Mitigation: Do not submit confidential designs, formulas, source code, or trade secrets without organizational approval for that service.

Risk: A user-supplied API key could be sent to an untrusted endpoint if the service URL is changed.

Mitigation: Keep PATENTMAX_BASE_URL unset or configure it only to the trusted PatentMax endpoint when using your own key.

Risk: Preliminary design-around ideas may not resolve patent infringement or jurisdiction-specific legal questions.

Mitigation: Have a qualified patent professional review the relevant claims and jurisdictions before implementing a design.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/patent-design-around)
- [PatentMax API documentation](https://api.ip930.com/features/api-platform)
- [Patent search workflow](references/search-workflow.md)
- [Patent query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Guidance, CSV file]

**Output Format:** [Markdown summary and UTF-8 CSV with BOM]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes claim features, proposed alternatives, related patent search results, and a notice that the ideas are not legal advice.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
