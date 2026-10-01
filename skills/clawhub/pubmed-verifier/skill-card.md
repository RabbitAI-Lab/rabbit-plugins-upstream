## Description:

Checks PMID, DOI, and arXiv citations against academic registries to flag mismatched, invalid, or retracted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit references in manuscripts, AI-generated writing, and knowledge bases before publication or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, or extracted citation context and optional contact or API-key attribution may be sent to academic registries.

Mitigation: For confidential manuscripts, limit --source to the necessary files and provide optional credentials or contact details only when appropriate.

Risk: Citation data may remain in the local cache or in generated reports and exports.

Mitigation: Use --no-cache for sensitive work and handle generated files according to the manuscript's confidentiality requirements.

Risk: Chosen report or export paths can overwrite existing files.

Mitigation: Select output and export filenames that do not contain important files.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [PubMed API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, Reports, Bibliography files]

**Output Format:** [Terminal text; HTML, JSON, or CSV reports; optional BibTeX export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts, retraction flags, and optional audit trails and comparison reports.]

## Skill Version(s):

3.2.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
