## Description:

Analyzes frontal face images or videos with a cloud health-risk service to produce early screening reports and alerts for conditions such as heart attack, stroke, hypertension, and hyperlipidemia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and care-setting operators use this skill to submit frontal face media to the Smyx/Life Emergence cloud service and receive structured early health-risk screening reports or historical report lists. It is intended for screening support and does not replace professional medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial images or videos and health-risk screening results may be sent to the Life Emergence/Smyx cloud service.

Mitigation: Use only with appropriate consent and avoid sensitive patient data unless the publisher provides clear privacy, retention, deletion, endpoint, and authentication controls.

Risk: The skill can query report history and uses persistent identity/account data and tokens.

Mitigation: Install only in trusted workspaces and review account, token storage, and access controls before production use.

Risk: Screening reports may be mistaken for medical diagnosis.

Mitigation: Treat outputs as early screening support only and route high-risk findings to qualified medical professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-health-risk-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON report content, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local face media or submit media URLs to a cloud API; can also return cloud report history for the resolved account identity.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
