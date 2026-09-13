## Description:

Analyzes nighttime child bedroom audio and video to detect bedtime crying, fear-of-the-dark behavior, nightmare awakenings, and out-of-bed events, then returns structured reports and soothing-action guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and integrators use this skill to analyze child bedroom nighttime media for signs of distress and to produce structured reports, recommended soothing actions, and historical report views. It is intended for child sleep-monitoring and caregiver-assistance workflows, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child audio/video and night reports may be processed or retained without enough user-facing disclosure.

Mitigation: Require clear documentation of processing location, retention, deletion controls, and caregiver consent before deployment.

Risk: The skill may silently create or reuse identities and query cloud history.

Mitigation: Require explicit opt-in for account creation and cloud history access, with visible controls to disable or delete stored records.

Risk: Tokens may be stored locally in plaintext SQLite.

Mitigation: Require token storage to use an approved secure store or encrypted storage before use with sensitive child-related data.

Risk: Private or development HTTP service endpoints may be used by default.

Mitigation: Require the publisher to remove private endpoints and document the production endpoints used by the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured report text, Markdown tables for history views, or JSON-style analysis depending on detail mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected event labels, soothing actions, recommendations, report links, and optional saved output files.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
