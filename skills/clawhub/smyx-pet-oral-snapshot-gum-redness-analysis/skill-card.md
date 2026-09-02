## Description:

This skill analyzes pet oral snapshot images or videos through remote APIs to report visible gum color, gum redness level, tartar coverage, and related oral-health observations without providing diagnosis or treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and pet-health platform teams use this skill to submit pet mouth images, videos, or media URLs for standardized oral-health observations and report links. It is also used to query cloud report history associated with the automatically selected identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or media URLs are sent to remote services for analysis.

Mitigation: Use only when the user accepts remote processing and trusts the publisher and service endpoints.

Risk: Cloud report history is queried using an automatically chosen identity.

Mitigation: Confirm that history access is expected for the deployment and that identity handling matches the user's consent and privacy requirements.

Risk: Identity and token data may be stored locally.

Mitigation: Review local storage behavior before deployment and prefer scoped credentials with minimal persisted account fields.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Analysis API Error Codes](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown and JSON analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
