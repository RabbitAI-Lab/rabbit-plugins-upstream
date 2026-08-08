## Description:

Analyzes full-plant images or videos to estimate wilting severity from visual posture indicators, optionally using soil-moisture context to distinguish likely underwatering from overwatering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and gardening or greenhouse operators use this skill to submit plant media for wilting quantification, likely cause assessment, intervention-direction guidance, and cloud report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-connected analysis may upload plant media or submit media URLs to a third-party service.

Mitigation: Review network/service use before installation and avoid submitting sensitive images, videos, URLs, or surrounding scene details.

Risk: The skill creates or reuses identity/session values and persists service tokens locally.

Mitigation: Run in an isolated workspace or user profile, review persisted account data after use, and clear local tokens when continued service association is not desired.

Risk: History report lookup can retrieve prior cloud-stored analysis records associated with the resolved identity.

Mitigation: Use only with accounts and environments where report history access is expected, and avoid sharing generated report links outside the intended audience.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Plant Wilting API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and structured JSON-like analysis reports, with optional report links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write an analysis result file when an output path is supplied; historical report queries return a structured report list.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
