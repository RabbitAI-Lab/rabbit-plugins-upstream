## Description:

Helps scholars improve the clarity and naturalness of Chinese and English academic drafts through local style checks, guided revision, mechanical cleanup, and integrity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and academic authors use this skill to review and revise their own Chinese or English manuscripts, remove mechanical writing artifacts, and check that edits preserve numbers, citations, and terminology. It is a writing-quality aid, not an authorship detector or substitute for required AI-use disclosure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rewriting could be misused to conceal AI assistance or misrepresent authorship.

Mitigation: Use only for legitimate editing of drafts and make any disclosure required by the institution or journal; never treat a style score as proof of authorship.

Risk: Automated cleanup or revision could change important manuscript content.

Mitigation: Review edits against the original and run integrity checks for numbers, citations, and terminology before submission.

Risk: Local runs may write manuscript reports and a persistent false-positive guard file.

Mitigation: Choose output paths deliberately and review generated files and the persistent user_guards.json file when handling sensitive drafts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Capability and detection boundaries](references/honest_boundaries.md)
- [Academic integrity and disclosure guidance](references/compliance.md)
- [Permissions and local file handling](references/permissions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown guidance and locally generated text, JSON, HTML, or CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional revision plans, cleaned drafts, and before/after integrity reports; PDF reading is experimental and needs manual review.]

## Skill Version(s):

3.5.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
