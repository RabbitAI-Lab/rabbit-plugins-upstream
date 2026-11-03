## Description:

A bilingual Chinese and English toolkit that helps authors review academic writing style, clean mechanical residue, plan revisions, and check whether key values and citation identifiers survived editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and academic authors use it to inspect writing patterns, clean mechanical residue, prepare focused revisions, and compare a draft with its revision. Authors review proposed edits and remain responsible for scientific accuracy and required AI-use disclosure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says integrity checks may still approve changed scientific values, and terminology replacement can damage citation identifiers.

Mitigation: Work on copies and separate outputs; manually compare scientific values, citation identifiers, and each terminology replacement before adopting a draft.

Risk: Reports and saved terminology exceptions remain on disk.

Mitigation: Choose intended output locations and review retained reports and exception files.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Best practices](references/best_practices.md)
- [Compliance and disclosure](references/compliance.md)
- [Honest boundaries](references/honest_boundaries.md)
- [PDF confidence limits](references/pdf_confidence.md)
- [Permissions and environment](references/permissions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, JSON, CSV, HTML]

**Output Format:** [Revised text files, Markdown plans and reports, and optional JSON, CSV, or HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local CLI workflow; PDF support is experimental. Review proposed edits and manually verify scientific values, citation identifiers, and terminology.]

## Skill Version(s):

5.2.0 (source: server release metadata; SKILL.md feature status)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
