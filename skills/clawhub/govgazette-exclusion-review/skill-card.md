## Description:

Review federal exclusion evidence for a business or person using GovGazette when the user asks about a potential SAM exclusion, debarment or suspension match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing potential federal exclusion matches use this skill to check a business or person against GovGazette and assess cited records, identity evidence and source freshness without treating a possible match as an eligibility decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exclusion lookups may send names or public identifiers to the remote GovGazette service.

Mitigation: Avoid confidential bid material and private credentials in queries.

Risk: Name-only matches or stale or unavailable sources can mislead eligibility decisions.

Mitigation: Verify identity against dated official sources, retain freshness warnings and do not treat a possible match or no match as a final eligibility determination.

## Reference(s):

- [GovGazette MCP service](https://govgazette.com/mcp)
- [GovGazette Exclusion Review on ClawHub](https://clawhub.ai/mooshee/skills/govgazette-exclusion-review)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites records and dated official sources; preserves stale or unavailable-source warnings.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
