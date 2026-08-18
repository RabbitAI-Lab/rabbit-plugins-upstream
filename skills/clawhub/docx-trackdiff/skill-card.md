## Description:

Compare two versions of a .docx document and produce a single Word file with native tracked changes that can be accepted or rejected in Word.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stephenlzc](https://clawhub.ai/user/stephenlzc)

### License/Terms of Use:

MIT

## Use Case:

External users, employees, and developers use this skill to compare two valid DOCX drafts and generate a local Word redline with native insertion and deletion revisions. It is suited to papers, reports, contracts, and other document review workflows where changes need to be accepted or rejected in Word.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DOCX drafts may contain sensitive text or embedded media.

Mitigation: Run the skill only on explicitly named local files and avoid sharing generated redlines outside the intended review workflow.

Risk: High-stakes reviews may depend on visual or structural fidelity beyond text comparison.

Mitigation: Run the bundled verifier and inspect the generated document in Word's All Markup view before relying on it.

Risk: Comments and footnote content are not diffed, and some image or equation paragraphs may fall back to whole-paragraph revisions.

Mitigation: Check comments, footnotes, images, and equations manually when those parts are material to the review.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/stephenlzc/docx-trackdiff)
- [ClawHub skill page](https://clawhub.ai/stephenlzc/skills/docx-trackdiff)
- [OOXML revision rules](references/ooxml-revision-rules.md)
- [Evaluation report](EVALUATION.md)

## Skill Output:

**Output Type(s):** [files, shell commands, guidance]

**Output Format:** [DOCX file with native Word revisions, plus concise Markdown status and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-selected DOCX files; verifier reports revision counts and pass/fail checks.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
