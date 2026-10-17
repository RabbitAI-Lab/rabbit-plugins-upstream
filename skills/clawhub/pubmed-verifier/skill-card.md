## Description:

Checks cited PMIDs, DOIs, and arXiv IDs against scholarly records, identifies mismatched or retracted citations, and prepares audit reports and formatted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit reference lists and AI-generated citations before publication or reuse, compare claimed paper details with scholarly records, and export reports or formatted bibliographies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, and optional contact email or API key are sent to academic lookup services.

Mitigation: Use the skill only when those disclosures are acceptable; provide contact and API-key parameters only when needed.

Risk: Broad input paths may expose unintended local documents, and citation results may remain in a local cache.

Mitigation: Select explicit input and output paths; use --no-cache when lookup results should not be retained locally.

Risk: Heuristic parsing, missing metadata, network outages, or cached retraction status can leave citations uncertain.

Mitigation: Provide expected titles through --claims-file for consequential decisions, review uncertain results, and run a final check with --no-cache.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [Python API reference](references/python_api.md)
- [Academic API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Formatted references]

**Output Format:** [Terminal text or optional HTML/JSON reports, with CSV, BibTeX, RIS, and formatted reference-list exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts with supporting evidence; unavailable lookups remain unverified.]

## Skill Version(s):

4.9.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
