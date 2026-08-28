## Description:

Supports identifying high-risk behaviors and health risks in videos or images, including falls, abnormal behavior, and visual signs associated with heart attack or stroke precursors, then returns alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-team operators use this skill to analyze uploaded videos, images, or stream URLs for fall, abnormal-behavior, and health-risk indicators and to retrieve structured report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive videos, images, stream URLs, and report history may be sent to configured lifeemergence.com cloud services.

Mitigation: Use only with appropriate consent, privacy review, and retention controls; avoid private medical, household, or camera footage unless the deployment policy covers it.

Risk: The skill can create or reuse cloud-linked identity and token data associated with the workspace.

Mitigation: Review workspace data ownership, local token storage, access controls, and cleanup procedures before installation.

Risk: Server-side security evidence classifies the release as Review before installation.

Mitigation: Require a human security review before enabling the skill in production or shared agent environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-risk-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Risk categories reference](references/risk_categories.md)
- [API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Structured text or JSON report, often presented in Markdown with report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk category, confidence, recommendations, and report export links; can list prior cloud report records.]

## Skill Version(s):

999.999.1005 (source: server release metadata; artifact frontmatter: 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
