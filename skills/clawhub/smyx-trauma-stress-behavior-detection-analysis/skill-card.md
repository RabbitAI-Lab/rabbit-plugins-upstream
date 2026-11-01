## Description:

Using fixed cameras in emergency shelters, the system analyzes video of disaster-affected crowds to identify visible behaviors associated with acute stress and produce alerts for on-site psychological rescue teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Emergency response teams use the skill to review shelter footage for visible stress-related behaviors and prepare structured observations and alerts to support welfare checks. Deployment guidance calls for authorization by an emergency command center or health authority and use alongside qualified psychological rescue personnel.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Sensitive shelter footage may still be uploaded when export-only mode is selected.

Mitigation: Before using real footage, require this behavior to be fixed and confirm the upload destination and the provider's deletion and privacy controls.

Risk: Remote enrollment and account or credential handling may lack clear user control or protection.

Mitigation: Require explicit control over remote enrollment, keep secrets separate from account identifiers, and store tokens securely.

Risk: Behavior alerts could prompt inappropriate rescue dispatch if treated as definitive findings.

Mitigation: Require qualified human review before escalating alerts or dispatching responders.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference (placeholder documentation)](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured behavior observations, alert details, recommendations, and report links; history can be summarized in a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual behavior observations only; the skill documentation prohibits clinical diagnosis and calls for human review of high-risk alerts.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
