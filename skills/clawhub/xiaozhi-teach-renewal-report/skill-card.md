## Description:

Drafts evidence-based student progress reports and renewal suggestions from learning records, with consent checks before parent-facing content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent tutors use this skill to turn one student's recorded lessons, homework follow-ups, progress evidence, and course balance into a stage report and a measured renewal suggestion. The teacher reviews drafts and decides whether and how to share them.

### Deployment Geography for Use:

China (mainland; localize crisis and compliance guidance for other regions)

## Known Risks and Mitigations:

Risk: Reports use minors' longitudinal learning records, and sharing without the required permissions could expose private information.

Mitigation: Use only the named student's relevant records, check parentCommunicationAllowed before parent-facing content, check emotionSharingWithParent before including classroom-state details, and have the teacher review drafts before manual sharing.

Risk: Unsupported figures or progress claims could mislead families.

Mitigation: Tie each number and progress statement to recorded evidence; use qualitative judgments when topic-level scores are absent, and avoid promises about outcomes.

## Reference(s):

- [Stage report templates](references/stage-report-templates.md)
- [Renewal communication scripts](references/renewal-communication-scripts.md)
- [Shared vocabulary and consent definitions](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown report drafts, progress summaries, and renewal communication scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed drafts; reports are not sent automatically.]

## Skill Version(s):

2.12.6 (source: server-resolved release version and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
