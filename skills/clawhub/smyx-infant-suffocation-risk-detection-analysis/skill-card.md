## Description:

Analyzes infant crib camera video or video URLs to identify sleep posture, mouth or nose occlusion, risk level, and report links for caregiver review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and childcare monitoring teams use this skill to submit infant crib video for auxiliary sleep-position and airway-occlusion risk analysis. The output supports monitoring workflows and does not replace adult supervision or medical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant videos or video URLs are sent to the publisher's backend for analysis.

Mitigation: Use only videos collected with guardian consent and deploy only where backend processing, retention, encryption, and access controls have been reviewed.

Risk: The skill silently creates or reuses an account identity, stores tokens locally, and can retrieve cloud report history.

Mitigation: Run it only in environments where local token storage and history access are acceptable, isolate the runtime, and clear stored credentials when access should end.

Risk: The analysis concerns infant safety and may be incomplete or incorrect.

Mitigation: Treat results as an auxiliary monitoring signal, verify alerts directly, and do not use the skill as a substitute for adult supervision or medical guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-suffocation-risk-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant suffocation risk API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON report text with risk fields and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sleep posture, face occlusion, occlusion object, risk level, event timing, snapshots, alert text, and report export URLs.]

## Skill Version(s):

1.0.4 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
