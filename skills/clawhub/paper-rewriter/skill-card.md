## Description:

Helps scholars revise Chinese and English academic drafts for clearer prose using local style checks, deterministic cleanup, and integrity checks for facts and terminology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars and academic writers use this skill to self-check and improve Chinese or English drafts, clean mechanical writing artifacts, and review whether revisions preserve numbers, citations, and terminology.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rewriting may misstate findings or change protected facts and terminology.

Mitigation: Review each revision manually and run the integrity checks against the original draft.

Risk: A style score may be mistaken for proof of authorship or detector status.

Mitigation: Treat scores as local style heuristics for self-review, not as an authorship finding.

Risk: Editing assistance may be used without required academic AI-use disclosure.

Mitigation: Edit only drafts you are authorized to change and retain disclosures required by the institution or journal.

Risk: Explicit output paths write files, and learned false-positive guards can persist locally.

Mitigation: Review output paths before running commands and inspect or remove locally saved guards when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [English style guide](artifact/references/style_guide_en.md)
- [Chinese style guide](artifact/references/style_guide_zh.md)
- [Academic integrity and disclosure guidance](artifact/references/compliance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown; optional JSON and HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local style scores are heuristics, not authorship or detector verdicts; users review revisions and integrity checks.]

## Skill Version(s):

3.3.0 (source: server-resolved release and skill documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
