## Description:

测评设计师 helps Chinese-language teachers design standards-aligned exams from two-way specification tables, controlled difficulty and cognitive-level ratios, item selection or adaptation, scoring rubrics, and post-exam review lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language school teachers use this skill to plan diagnostic, formative, and summative assessments with explicit knowledge-point coverage, difficulty bands, cognitive levels, item sources, and scoring standards. It also helps prepare item-revision and review-priority lists while leaving post-exam statistical calculation and lesson planning to adjacent skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-generated or skill-generated exam items may contain incorrect answers, unclear wording, inappropriate difficulty, or weak alignment with the blueprint.

Mitigation: Require teacher review before formal use; label AI-generated items and keep them out of final exams until the teacher has solved them, checked answers and points, and marked them verified.

Risk: Assessment artifacts can accidentally include real student names or sensitive student details.

Mitigation: Keep real student names out of stored fields and written outputs, use pseudonyms or seat numbers, and honor the skill's view, correct, delete, pause-memory, and sharing controls.

Risk: Student text may reveal crisis signals that are outside the scope of exam design.

Mitigation: Stop the exam-design workflow, avoid diagnosis or detailed probing, direct the user to trusted adults and local emergency or crisis contacts, and record only the referral action if anything is stored.

Risk: Copied workbook, teaching-aid, or past-exam items can create copyright or licensing concerns.

Mitigation: Track copyrightStatus for each item, prefer teacher-owned or original material, document adaptation points, and store restricted third-party questions only as indexes rather than full copied text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Exam blueprint and specification-table template](references/exam-blueprint.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item self-check protocol](shared/ai-item-check.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown tables, structured text templates, and JSON-compatible classWorkspace field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs scoring standards rather than automatic grading; AI-generated items are labeled for teacher verification before formal use.]

## Skill Version(s):

2.1.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
