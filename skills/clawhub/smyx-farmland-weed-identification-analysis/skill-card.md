## Description:

Analyzes field images or videos to identify weeds, estimate coverage density, and provide weed distribution data and reports for precision weeding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm managers and agricultural advisers use field images or video to assess weed species, coverage, and pressure across crop fields, and to review past analysis reports. Results support field management decisions but do not prescribe herbicide use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Field images or video are sent to a remote service for analysis.

Mitigation: Share only approved field media and confirm the service's data-handling terms before use.

Risk: The skill automatically creates or reuses an account identity and stores returned tokens in a local SQLite database.

Mitigation: Review or remove automatic identity setup and token persistence before use in shared or automated environments.

Risk: Cloud report retrieval has scoping problems and could expose report history outside the intended identity.

Mitigation: Verify account isolation and authorization before enabling report-history queries.

## Reference(s):

- [Farmland weed analysis API documentation](references/api_doc.md)
- [Analysis service API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include weed coverage estimates, distribution data, and report links.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
