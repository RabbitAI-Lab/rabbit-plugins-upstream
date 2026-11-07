## Description:

Analyzes pet monitoring images and videos for feeding, drinking, elimination, activity, vomiting, and mobility indicators, then returns health-monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care teams can review monitoring footage for changes in routine behavior and retrieve previous reports. The reports are for reference and do not replace veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may still upload private videos.

Mitigation: Assume private footage may be uploaded; avoid sensitive footage until this is fixed and verify the actual destination before use.

Risk: Account credentials lack adequate safeguards.

Mitigation: Use a dedicated service account in an isolated workspace, and have credential destination checks fixed before sending sensitive footage.

Risk: External service behavior and retention are unverified, and usage may incur charges.

Mitigation: Confirm the provider's data-retention policy and possible charges before sending footage.

## Reference(s):

- [API reference (Chinese)](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured health-monitoring report; historical report listings use a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include monitored behavior indicators, risk notices, recommendations, and report links.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
