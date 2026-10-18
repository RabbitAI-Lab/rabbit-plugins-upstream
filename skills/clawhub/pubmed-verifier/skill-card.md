## Description:

Verifies scholarly citations against academic registries, flags mismatched or retracted references, and prepares citation audit reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, editors, and developers use this skill to check PMIDs, DOIs, arXiv IDs, and reference lists for citation errors before publication or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and some extracted titles from selected files may be sent to external academic registries.

Mitigation: Select narrow input paths when checking private work and review material before submitting it for verification.

Risk: Local reports and a verification cache may retain citation information.

Mitigation: Review export paths and use --no-cache when a persistent local cache is not wanted.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [Python API reference](references/python_api.md)
- [Academic registry API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Citation-verification guidance and text reports; optional HTML, JSON, CSV, BibTeX, RIS, or formatted reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts with supporting metadata; optional local audit exports]

## Skill Version(s):

5.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
