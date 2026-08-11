## Description:

Analyzes emergency-shelter video to flag visual acute-stress behaviors such as stupor, tremor, unresponsiveness, and hypervigilance, producing behavior-observation alerts for authorized psychological-rescue teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External emergency-response operators and authorized psychological-rescue teams use this skill to review fixed-camera shelter video, identify visual behavior signals associated with acute stress, and prioritize human follow-up. The output is a behavior-observation alert and response aid, not a clinical diagnosis.

### Deployment Geography for Use:

Global, subject to local emergency-response, mental-health, privacy, and video-surveillance requirements.

## Known Risks and Mitigations:

Risk: Sensitive shelter video and report metadata may be processed by configured cloud services.

Mitigation: Deploy only with explicit emergency-response authorization, documented retention rules, access controls, and operator acceptance of the external processing path.

Risk: Locally retained generated or returned identity/token data could expose response context or access credentials.

Mitigation: Restrict workspace access, rotate credentials where applicable, and review local storage before and after operational use.

Risk: Behavior alerts could be mistaken for clinical diagnoses or used for automatic dispatch decisions.

Mitigation: Treat outputs as visual behavior observations only; require qualified human review before escalation, intervention, referral, or rescue dispatch.

Risk: Unredacted public display or long retention of disaster-affected people can create privacy and dignity harms.

Mitigation: Blur faces on command displays, avoid non-rescue reuse, and delete raw video according to the stated short-retention policy.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Shell commands]

**Output Format:** [Structured analysis report or history table with observed behavior signals, crisis level, response guidance, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include temporary tracking identifiers, zone locations, PFA quick-reference guidance, and recommendations for human review.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
