## Description:

A bilingual academic writing toolkit that checks style, cleans mechanical artifacts, guides clearer revisions, and checks that numbers, citations, and terminology survive edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors, especially bilingual and non-native English writers, use this skill to identify formulaic prose, plan clearer revisions, and check that edits preserve cited identifiers, figures, and terminology. It supports writing self-review, not authorship assessment or required AI-use disclosure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Style scores may be mistaken for evidence of AI authorship.

Mitigation: Treat scores as editing prompts only; review the text and do not draw authorship conclusions.

Risk: Rewriting may be misused to conceal AI assistance or evade academic-integrity review.

Mitigation: Use it for legitimate quality editing, meet applicable disclosure requirements, and review generated changes before submission.

Risk: Learned terminology exceptions may affect the reliability of later self-check reports.

Mitigation: Review learned user_guards.json entries before relying on reports for submission workflows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Honest boundaries](references/honest_boundaries.md)
- [Deep rewrite guide](references/deep_rewrite_guide.md)
- [PDF confidence](references/pdf_confidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Plain text and Markdown revisions or reports; optional HTML, JSON, and CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local files and integrity-check exit codes; PDF extraction is experimental.]

## Skill Version(s):

3.5.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
