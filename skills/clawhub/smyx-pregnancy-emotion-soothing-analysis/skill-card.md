## Description:

Analyzes fixed-camera and optional microphone inputs from pregnancy home or prenatal waiting-room settings to identify emotion-related behaviors and produce structured soothing recommendations and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-support teams use this skill to analyze pregnancy-related audio or video inputs for observable emotional fluctuation signals, soothing-action suggestions, and historical report lookup. It is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive pregnancy-related camera and optional microphone data.

Mitigation: Use only with explicit consent from the pregnant person and other recorded people, and document retention and deletion behavior before deployment.

Risk: The security evidence says default networking, account handling, token storage, and automatic notification behavior are not safely scoped.

Mitigation: Review the skill carefully before installation, replace bundled development HTTP endpoints with production HTTPS endpoints, and verify account, token, and recipient controls.

Risk: The skill may disclose inferred emotional state to family members or emergency contacts.

Mitigation: Configure escalation recipients intentionally, disclose notification behavior to affected users, and confirm opt-out or override processes for shared spaces.

Risk: Emotion analysis in pregnancy contexts can be mistaken for medical assessment.

Mitigation: Present outputs as observed behavior and support guidance only, and route repeated or urgent concerns to qualified prenatal mental-health or medical resources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis)
- [Pregnancy Emotion Soothing API Documentation](artifact/references/api_doc.md)
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured text reports, with optional JSON-oriented detail and saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observed event summaries, soothing recommendations, historical report tables, and report links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
