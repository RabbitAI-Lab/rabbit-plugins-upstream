## Description:

A bilingual academic-writing toolkit that checks for formulaic phrasing, cleans mechanical artifacts, and guides revisions while checking that key numbers, citations, and terms remain intact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and academic writers use it to review and revise Chinese or English manuscripts, clean mechanical writing artifacts, and check that important numbers, citations, and terminology survive edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Style scores are local heuristics: they may miss fluent model-generated text and may flag conventional academic prose.

Mitigation: Treat scores as self-review prompts, not as evidence of authorship or proof that text was human-written.

Risk: Term unification can replace variants incorrectly, and DOCX write-back does not rebuild tables, images, or styles.

Mitigation: Keep the original draft, review replacement counts and every changed passage, and inspect DOCX output; merge complex layouts manually.

Risk: The documented stdout mode may not return revised text, and reports can contain manuscript content.

Mitigation: Use an explicit separate output path, review the result and warnings, and handle reports as confidential manuscript material.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Project repository (linked by the supplied README)](https://github.com/docsor1212/paper-rewriter)
- [Reading map and documentation index](references/INDEX.md)
- [Honest boundaries](references/honest_boundaries.md)
- [Permissions and environment](references/permissions.md)
- [Compliance guidance](references/compliance.md)
- [Feature status](references/feature_status.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Revised text files, Markdown reports and plans, and agent-facing revision guidance; optional DOCX output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and require human review; DOCX write-back preserves plain paragraphs, not complex layout.]

## Skill Version(s):

5.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
