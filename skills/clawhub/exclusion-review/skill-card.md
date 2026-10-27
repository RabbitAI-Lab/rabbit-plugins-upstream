## Description:

Review federal exclusion evidence for a business or person using GovGazette when the user asks about a potential SAM exclusion, debarment or suspension match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, compliance, and contracting teams use this skill to review possible federal SAM exclusions, suspensions, or debarments through GovGazette and dated official evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send submitted names or identifiers to GovGazette.

Mitigation: Share only the minimum necessary information, keep credentials and confidential bid material out of queries, and review GovGazette's privacy policy.

Risk: Possible matches, stale records, or missing records may be mistaken for confirmed exclusion or clearance.

Mitigation: Check source status and freshness, verify dated official evidence, describe name-only or conflicting-identifier results as possible matches, and state that no match is not clearance.

## Reference(s):

- [GovGazette](https://govgazette.com)
- [GovGazette MCP service](https://govgazette.com/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries with citations to records and dated official sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source status and freshness warnings; distinguishes possible matches from eligibility determinations.]

## Skill Version(s):

1.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
