## Description:

A bilingual Chinese and English toolkit for self-checking and naturalizing academic prose, cleaning model artifacts, and guiding revisions with integrity checks and disclosure safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and academic writers use the toolkit to review and improve Chinese or English academic drafts, clean writing artifacts, and prepare revision reports. It supports author review and disclosure-aware editing, not authorship misrepresentation or evasion of integrity review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's checks can approve altered research data, and terminology replacement can corrupt citation identifiers.

Mitigation: Work on copies with separate output filenames. Manually review every changed number, citation identifier, and terminology replacement; a PASS result does not prove that all data survived unchanged.

Risk: Numeric checks and identifier protection are not suitable for unattended acceptance gates until corrected; the write manifest is not a complete audit.

Mitigation: Avoid unattended acceptance gates. Use an explicit -o output path rather than redirecting transform output, and do not treat the manifest as a complete audit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [GitHub project page (linked from README)](https://github.com/docsor1212/paper-rewriter)
- [ModelScope mirror](https://modelscope.cn/skills/Docsor/paper-rewriter)
- [Academic integrity and disclosure guidance](artifact/references/compliance.md)
- [Honest boundaries](artifact/references/honest_boundaries.md)
- [Feature status and limitations](artifact/references/feature_status.md)
- [Python API reference](artifact/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Revised academic prose, text or DOCX drafts, and Markdown reports or revision plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese and English; output depends on the selected workflow.]

## Skill Version(s):

5.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
