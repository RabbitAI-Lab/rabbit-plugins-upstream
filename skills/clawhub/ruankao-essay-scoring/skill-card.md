## Description:

Scores and diagnoses Ruankao advanced qualification essays across five tracks, using rubric-based checks for topic fit, professional depth, practical evidence, writing quality, and structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nieen](https://clawhub.ai/user/nieen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate Ruankao advanced essay drafts, confirm the target qualification track, identify scoring weaknesses, and receive focused improvement guidance before revision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect essay text supplied by the user.

Mitigation: Use it only with essay content the user is comfortable sharing with the active agent environment.

Risk: The declared Write/Edit capability is broader than basic scoring needs.

Mitigation: Review proposed file writes or edits before accepting them, and run the skill in contexts where report-file creation or editing is expected.

Risk: Scoring guidance can be inaccurate or misleading if the wrong qualification track or essay prompt is used.

Mitigation: Confirm the target qualification and original essay prompt before relying on the scoring report.

## Reference(s):

- [Ruankao Essay Scoring skill page](https://clawhub.ai/nieen/skills/ruankao-essay-scoring)
- [Default scoring rubric](artifact/references/scoring-rubric.md)
- [Project management scoring rubric](artifact/references/scoring-rubric-pm.md)
- [System analyst scoring rubric](artifact/references/scoring-rubric-sa.md)
- [Network planning scoring rubric](artifact/references/scoring-rubric-ne.md)
- [System planning and management scoring rubric](artifact/references/scoring-rubric-sp.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown scoring report with tables and targeted revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-dimension scores, word count, seven-question coverage checks, pass-line status, and prioritized improvement suggestions.]

## Skill Version(s):

1.2.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
