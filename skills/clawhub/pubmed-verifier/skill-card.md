## Description:

Checks cited PMIDs, DOIs, and arXiv IDs against publication records, flags mismatched or retracted citations, and prepares citation audit reports and formatted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to check reference lists and AI-generated citations against publication records before sharing or submitting work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning a broad directory can read unrelated private documents, and citation identifiers or titles may be sent to public academic registries.

Mitigation: Use explicit file paths and avoid folders containing unrelated private documents; review what will be queried before running.

Risk: Cached results may miss recent publication or retraction updates.

Mitigation: Use --no-cache for the final citation check before submission.

Risk: Registry requests may include a supplied API key or contact email.

Mitigation: Provide NCBI_API_KEY or PUBMED_VERIFIER_MAILTO only if you want those values used for registry requests.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Usage guide](artifact/references/usage_guide.md)
- [Python API reference](artifact/references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance and command examples; citation reports in text, JSON, HTML, or CSV; optional formatted reference lists and bibliography exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish correct, mismatch, partial, invalid, and unknown citations and can include per-citation evidence.]

## Skill Version(s):

4.8.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
