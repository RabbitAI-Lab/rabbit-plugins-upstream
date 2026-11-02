## Description:

Analyzes fixed-camera video of a water-cup area to count pickup events as an indirect proxy for drinking frequency and flag low counts for caregiver follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and care teams can use the skill to review cup-pickup frequency from home or care-facility video and identify patterns that may warrant checking in or encouraging hydration. Counts are an indirect behavioral signal, not a medical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option may still run an analysis.

Mitigation: Do not treat it as a dry run; confirm the behavior before using the option.

Risk: Authenticated requests may be sent without safeguards restricting their destinations.

Mitigation: Use only approved HTTPS destinations and review credential handling before connecting an account.

Risk: Remote account creation and video or report retention and deletion controls need confirmation.

Mitigation: Verify account creation, credential protection, and retention and deletion controls before sending footage.

Risk: Video of older adults is sensitive, and cup pickups do not prove that water was consumed.

Mitigation: Use footage only with informed consent, protect it appropriately, and treat counts as an indirect signal rather than a medical assessment.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results and report links; historical results are returned as JSON and can be presented in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cup-pickup counts, timing, baseline comparisons, and caregiver alerts; pickup counts are only an indirect proxy for water intake.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
