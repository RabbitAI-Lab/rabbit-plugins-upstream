## Description:

Checks whether PMID, DOI, arXiv, and other citation references exist and match the cited publication, then produces verification reports and formatted reference lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence-based medicine teams use it to batch-check PMIDs, DOIs, arXiv IDs, and reference lists against scholarly registries, catch mismatches and retractions, and export reports or formatted citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proxy diagnostics may expose credentials embedded in a proxy URL.

Mitigation: Redact credentials before sharing --doctor output.

Risk: Existence-only checks and invalid DOI verdicts can be overinterpreted.

Mitigation: Supply expected citation metadata and independently review these results before relying on an audit.

Risk: Identifiers, citation search terms, and configured contact email are sent to scholarly services.

Mitigation: Exclude confidential details and choose a narrow source directory.

Risk: Cached registry status may not reflect the latest retraction or DOI information.

Mitigation: Use --no-cache when fresh checks matter.

## Reference(s):

- [Usage guide](references/usage_guide.md)
- [Command-line flags](references/flags.md)
- [Python API](references/python_api.md)
- [API examples](references/api_examples.md)
- [Project homepage](https://github.com/docsor1212/pubmed-verifier)
- [ModelScope package mirror](https://modelscope.cn/skills/Docsor/pubmed-verifier)

## Skill Output:

**Output Type(s):** [Text reports, HTML reports, JSON reports, CSV, BibTeX, CSL JSON]

**Output Format:** [Terminal text, HTML or JSON reports, CSV, BibTeX, CSL JSON, and formatted reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize verification states and supporting citation metadata; formatted reference exports contain registry-verified entries with review sections for incomplete results.]

## Skill Version(s):

6.3.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
