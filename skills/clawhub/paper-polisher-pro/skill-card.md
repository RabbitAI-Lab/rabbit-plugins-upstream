## Description:

Locally checks academic manuscripts for AI-writing signals and disclosure labels, and offers writing-quality, terminology, and style guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Academic authors and editors use this skill to self-check manuscripts, review paragraph-level signals, improve clarity and terminology, and check AI-assistance disclosures before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manuscript content may be sensitive when selected for inspection or saved in reports.

Mitigation: Run only on files and directories you trust, and review where reports are written.

Risk: AI-writing scores can be misleading for short, mixed, English, or medical text.

Mitigation: Treat scores and paragraph signals as advisory, check the reported engine mode, and make decisions through human review rather than automated verdicts.

Risk: Optional supervised model files are supplied separately.

Mitigation: Use model files from a source you trust and verify them with the skill's setup check before use.

Risk: Polishing guidance could be misused to misrepresent AI-assisted writing.

Mitigation: Follow institutional AI-use and disclosure policies; use label checks to support transparent attribution.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)
- [Project documentation](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, HTML, Text]

**Output Format:** [Markdown and JSON reports, HTML paragraph reports, and command-line text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores are advisory; the optional supervised model is not bundled.]

## Skill Version(s):

4.7.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
