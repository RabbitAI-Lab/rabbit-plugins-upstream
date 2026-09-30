## Description:

Analyzes pet photos and videos for body-condition changes, visible injuries, skin abnormalities, and signs of unusual activity, then returns a health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and their agents use the skill to review pet images or videos for potential health concerns and retrieve past analysis reports. Results are informational and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, media URLs, generated user identifiers, and report history may be sent to a cloud service without a clear consent step.

Mitigation: Obtain explicit user consent before uploads or history queries, and confirm the configured service and its data handling are acceptable.

Risk: Account tokens are stored locally in the workspace, and the skill may silently create or reuse a user identity.

Mitigation: Restrict access to local tokens and document how identities and tokens are created, retained, and removed.

Risk: Broad triggers and bundled account/history helpers can invoke services beyond the requested pet analysis.

Mitigation: Narrow activation triggers and separate history and account actions from image and video analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Plain-text or JSON analysis reports, with Markdown links for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assessment findings, suggestions, and report links; can save output to a local file.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
