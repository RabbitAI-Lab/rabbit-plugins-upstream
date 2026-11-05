## Description:

A bilingual academic writing toolkit that helps scholars check stylistic patterns, clean drafts, plan revisions, and preserve key data and terminology during editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External scholars, especially authors working between Chinese and English, can use the toolkit to inspect stylistic patterns, clean mechanical residue, plan prose revisions, and check that numbers, identifiers, and terminology survive edits. Its style reports are diagnostic and do not determine whether text was written by AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Heuristic style reports can be mistaken for AI-authorship detection or proof of originality.

Mitigation: Use reports only to guide editing; follow the applicable disclosure rules and do not treat a score as an authorship verdict.

Risk: A rewrite or cleanup may alter scientific values, citations, or terminology even when an integrity check reports PASS.

Mitigation: Keep the original manuscript, review warnings, and manually compare values, citations, and terminology before using the edited draft.

Risk: Optional terminology unification can replace text inside identifiers, and DOCX write-back does not rebuild complex layout elements.

Mitigation: Review the full unification diff and use a separate output file; manually merge DOCX changes when tables, images, or styles need preservation.

## Reference(s):

- [Quick start and toolkit overview](README.md)
- [Academic integrity and disclosure guidance](references/compliance.md)
- [Honest boundaries and limitations](references/honest_boundaries.md)
- [Python API and command reference](references/api.md)
- [Source repository](https://github.com/docsor1212/paper-rewriter)
- [ModelScope skill page](https://modelscope.cn/skills/Docsor/paper-rewriter)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, HTML, JSON]

**Output Format:** [Revised academic prose, diagnostic reports, revision plans, and integrity-check results; format depends on the command used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file outputs; review proposed revisions and reports against the original manuscript before adopting them.]

## Skill Version(s):

5.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
