## Description:

Review federal exclusion evidence for a business or person using GovGazette when the user asks about a potential SAM exclusion, debarment or suspension match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to review a business or person's potential SAM exclusion, debarment, or suspension match. It helps summarize identity evidence and record details using dated official sources; it does not determine eligibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may expose sensitive identifiers or confidential bid information.

Mitigation: Query only names and identifiers the user is authorized to share, and keep private credentials and confidential bid material out of queries.

Risk: A name-only or conflicting-identifier result may be mistaken for a confirmed exclusion or eligibility decision.

Mitigation: Describe uncertain results as possible matches, verify them against dated official sources, and do not make eligibility determinations. A no-match result or a record missing from a later snapshot does not establish clearance or reinstatement.

## Reference(s):

- [GovGazette](https://govgazette.com)
- [GovGazette MCP](https://govgazette.com/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown summary with cited record and official sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports identity evidence, source status, dates, restriction type, agency, and official links when available.]

## Skill Version(s):

1.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
