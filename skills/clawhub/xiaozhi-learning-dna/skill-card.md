## Description: <br>
学习DNA helps agents maintain an opt-in, minimal student learning profile for personalized tutoring continuity, with controls to view, correct, delete, pause memory, and pause sharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners, guardians, and education agents use this skill to create and update a controlled long-term learning profile only after explicit consent. It supports personalized tutoring continuity, learning-style adaptation, growth milestones, cross-subject connections, and crisis referral handling without treating inferred emotional fields as clinical assessments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill maintains persistent student learning profiles and inferred emotional data. <br>
Mitigation: Use it only after explicit student or guardian opt-in, and confirm view, correct, delete, pause-memory, and pause-sharing controls are available. <br>
Risk: Automatic profile updates and cross-skill sharing can expand the amount of retained or shared student data. <br>
Mitigation: Keep emotion tracking, reminders, and cross-skill sharing disabled unless separately needed and explicitly authorized. <br>
Risk: Inferred learning-emotion fields could be mistaken for clinical or authoritative assessments. <br>
Mitigation: Treat emotion fields as learning-state observations only, avoid clinical labels, and follow the crisis referral protocol for safety signals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna) <br>
- [学习DNA template](references/dna-template.md) <br>
- [Crisis referral protocol](references/crisis-referral-protocol.md) <br>
- [Cross-subject concept connections](references/cross-subject-connections.md) <br>
- [Growth milestones reference](references/growth-milestones.md) <br>
- [学习DNA JSON Schema README](schemas/README.md) <br>
- [Published DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON schema definitions, reference templates, and validation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should remain consent-gated, privacy-minimized, and clearly labeled when conclusions are inferred from limited learning data.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
