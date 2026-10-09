## Description:

Book Breakdown turns a supplied book file, title, or link into structured reading notes with an overall summary, key concepts, chapter breakdown, action checklist, and optional visual HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yysws5566](https://clawhub.ai/user/yysws5566)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, reviewers, educators, and knowledge workers use this skill to turn books into concise summaries, concept notes, chapter maps, teaching material, reviews, and action checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read book files or links supplied by the user.

Mitigation: Use it only with reading material you are comfortable sharing with the agent, and request an offline-only response for sensitive content.

Risk: The skill may perform web lookups about books, authors, reviews, ratings, or linked pages.

Mitigation: Ask the agent to avoid web lookups when the task must remain private or when external sources should not influence the summary.

Risk: Generated HTML reports may include an external font link from the bundled template.

Mitigation: Remove the external font link or keep generated reports offline before opening them with network access.

Risk: Book summaries can omit nuance or misstate source material when the provided text, table of contents, or public information is incomplete.

Mitigation: Review summaries against the original book for important decisions, and require the agent to mark incomplete parsing or public-information-only analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yysws5566/skills/book-breakdown)
- [Publisher profile](https://clawhub.ai/user/yysws5566)
- [HTML report template](artifact/templates/book-report-template.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Structured Markdown notes and optional self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local book-note and report files; can use provided book files, titles, links, OCR inputs, and web lookups when available.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
