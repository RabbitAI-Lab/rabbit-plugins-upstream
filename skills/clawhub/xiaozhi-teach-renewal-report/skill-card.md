## Description:

Drafts evidence-based Chinese student progress reports and renewal guidance for independent teachers from a named student's learning records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to summarize one Chinese K–12 student's documented learning progress and draft a fact-based report, next-step plan, and optional renewal language for teacher review. Parent-facing drafts require the relevant consent checks and are sent manually by the teacher.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Longitudinal records about a minor may expose sensitive learning information or classroom observations.

Mitigation: Scope access to the named student and relevant records, omit identifying details, and check parentCommunicationAllowed and, for classroom-state content, emotionSharingWithParent before preparing parent-facing drafts.

Risk: Unsupported progress claims or pressured renewal language could mislead families.

Mitigation: Tie numerical claims to recorded evidence, use qualitative wording where scores are unavailable, and have the teacher review and manually send any parent-facing report or renewal message.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [Stage report templates](artifact/references/stage-report-templates.md)
- [Renewal communication scripts](artifact/references/renewal-communication-scripts.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language report drafts and suggested renewal wording]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed drafts; no automatic parent messaging or student-record changes beyond confirmed progress evidence.]

## Skill Version(s):

2.4.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
