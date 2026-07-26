## Description: <br>
Generates weekly learning review reports from authorized learning activity, including progress evidence, weak points, next-week priorities, and optional family-facing summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students and learning-support agents use this skill to turn weekly learning records into evidence-based review reports, concrete next-week priorities, and optional family-sharing summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weekly reviews may summarize learning activity, emotional state, stress, or crisis-related observations that are sensitive if shared too broadly. <br>
Mitigation: Use the skill only for an explicit review request, collect only the minimum necessary fields, and review family-facing reports before sharing. <br>
Risk: Crisis signals such as self-harm thoughts, bullying, serious harm, or sustained despair could be softened if treated like normal learning feedback. <br>
Mitigation: Do not reframe crisis signals as positive progress; alert guardians plainly and seek professional or emergency help when immediate danger is present. <br>
Risk: Sparse or incomplete weekly data can make conclusions sound more certain than the evidence supports. <br>
Mitigation: State when data is limited, identify which days or records support the review, and avoid firm judgments when evidence is incomplete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review) <br>
- [Weekly review report template](references/review-report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown learning review reports with structured sections and concise action recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce separate student-facing and family-facing report variants when appropriate.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
