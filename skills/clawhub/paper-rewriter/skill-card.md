## Description:

A bilingual Chinese and English toolkit for reviewing academic prose, cleaning mechanical artifacts, planning revisions, and checking that numbers, citations, and terminology survive editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, including non-native writers, use it to inspect and revise Chinese or English academic drafts for clarity and natural style while checking text integrity. Its style reports are heuristic self-review aids and do not determine authorship or whether text was written by AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because rewriting and integrity checks may alter protected terms or numeric values, and the scan coverage is partial.

Mitigation: Compare revised text with the source and carefully review changed numbers, DOIs, PMIDs, years, and terminology; use the integrity guard and inspect any flagged changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Publisher profile](https://clawhub.ai/user/docsor1212)
- [Project page linked by the package README (not server-resolved provenance)](https://github.com/docsor1212/paper-rewriter)
- [ModelScope mirror linked by the package README](https://modelscope.cn/skills/Docsor/paper-rewriter)
- [Skill usage and integrity boundaries](artifact/SKILL.md)
- [Honest boundaries](artifact/references/honest_boundaries.md)
- [Academic integrity and compliance guidance](artifact/references/compliance.md)
- [Python API reference](artifact/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown reports, HTML reports, CSV reports, JSON reports, Revised document files]

**Output Format:** [Plain text, Markdown, HTML, CSV, or JSON; optionally DOCX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written to selected file paths. DOCX write-back uses plain paragraphs and does not rebuild complex layouts.]

## Skill Version(s):

5.15.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
