## Description:

Review federal exclusion evidence for a business or person using GovGazette when the user asks about a potential SAM exclusion, debarment or suspension match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, compliance, and due diligence teams use this skill to review evidence of a possible federal exclusion, debarment, or suspension match and prepare a sourced summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Names and identifiers used in a lookup are sent to GovGazette.

Mitigation: Submit only identifiers needed for the check; keep credentials and confidential bid information out of queries.

Risk: A possible match, no match, or later snapshot could be mistaken for a definitive eligibility or reinstatement decision.

Mitigation: Verify dated official records, explain identity evidence and record scope, and state that no match is not clearance and a name-only match does not establish debarment.

## Reference(s):

- [GovGazette](https://govgazette.com)
- [GovGazette MCP](https://govgazette.com/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown report with identity evidence, record status, dates, restriction details, agency, and official links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A possible match or no match is not an eligibility determination or clearance.]

## Skill Version(s):

1.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
