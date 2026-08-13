## Description:

Estimates an indoor plant's relative transpiration rate from thermal or RGB leaf imagery plus optional environmental data, returning structured water-stress and root-activity guidance with report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, plant-care teams, greenhouse operators, and developers use this skill to estimate a relative transpiration-rate index for indoor plants from leaf images or videos, then review possible water stress, root-activity status, and care guidance. It also supports cloud-backed history lookup for prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant images, videos, or supplied media URLs to lifeemergence cloud services.

Mitigation: Use non-sensitive media and public or intentionally shared URLs unless the publisher clarifies retention, access, and deletion controls.

Risk: The skill silently creates or reuses an internal account identity and stores authentication tokens locally.

Mitigation: Run it only in a managed workspace where local data storage is access-controlled, and confirm token rotation and deletion procedures before deployment.

Risk: Cloud history lookup is tied to the internal identity used by the skill.

Mitigation: Inform users that report history is cloud-backed and verify account-scoped export, retention, and deletion controls.

Risk: Security evidence notes inconsistent pet/video documentation, which may confuse expected inputs and outputs.

Mitigation: Review the user-facing instructions and accepted parameters before production use so callers understand supported plant media and report behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-transpiration-rate-estimation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a caller-specified file; history queries return structured report-list content from the cloud API.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
