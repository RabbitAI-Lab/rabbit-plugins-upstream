## Description:

Detects morbid behavioral cues in poultry and pigs from barn images or continuous videos and returns structured behavior findings, risk levels, abnormal subject locations, group-level proportions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, farm operators, and developers can use this skill to screen poultry or swine barn media for early morbid behavior indicators and retrieve prior analysis reports. The output is for behavioral screening support and is not a veterinary diagnosis or treatment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock images, videos, report queries, and report identifiers are sent to provider cloud APIs.

Mitigation: Use the skill only where provider-side processing of barn media and report data is acceptable, and review data handling requirements before deployment.

Risk: Release configuration and bundled environment files include plaintext HTTP endpoints for development or web access.

Mitigation: Require HTTPS-only production endpoints and remove or disable plaintext development endpoints before installation in a sensitive environment.

Risk: The skill resolves account identity automatically and can store or reuse tokens locally.

Mitigation: Run in an isolated workspace, make identity handling explicit for the deployment, protect local token storage, and rotate credentials if exposure is suspected.

Risk: A payment-related error path can prompt installation or recharge steps for a payment skill.

Mitigation: Ensure any payment workflow is documented, user-confirmed, and removable from unattended execution paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sick-poultry-behavior-detect-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown and JSON-formatted structured analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior type, risk level, abnormal subject location, group morbidity ratio, analysis history, and report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
