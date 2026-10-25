## Description:

Analyzes flower-bud images or videos to estimate flowering dates and provide reports or cloud-based report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and horticulture teams use flower-bud imagery, optionally with temperature and light data, to estimate bloom timing and plan pollination, harvesting, or visitor activities. They can also retrieve prior reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted plant media and URLs are sent to configured LifeEmergence cloud services.

Mitigation: Confirm data-sharing authorization and review the destination services before submitting media or URLs.

Risk: The skill silently creates or reuses an identity, stores authentication tokens in a local workspace database, and retrieves cloud history associated with that identity.

Mitigation: Review local token storage and access to the linked cloud history before enabling the skill.

Risk: The bundled API documentation describes pet-health endpoints rather than flowering prediction.

Mitigation: Verify the applicable endpoints and correct the documentation before broad deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Bundled API reference (pet-health terminology; verify applicability)](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis report; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links; results can be saved to a file.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release; bundled SKILL.md says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
