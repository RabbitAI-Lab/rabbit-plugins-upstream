## Description:

Checks whether cited PMIDs identify the claimed papers, flags mismatches and retractions, and produces reviewable citation reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit PMID citations in manuscripts, evidence libraries, and AI-generated text before publication or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, DOIs, titles, and optional contact or API-key parameters are sent to public academic registries.

Mitigation: Use only with citation data suitable for those services and supply contact or API-key parameters only when appropriate.

Risk: Reports, audit files, and the local cache may retain citation context from sensitive documents.

Mitigation: Limit --source to intended files, use --no-cache for sensitive work, and review reports and audit files before sharing.

Risk: Heuristic context parsing or stale cached retraction information can leave citations needing manual review.

Mitigation: Use structured claims for precise comparisons, review partial or unknown verdicts, and run --no-cache before submission.

## Reference(s):

- [PubMed E-utilities API quick reference](references/api_examples.md)
- [PubMed Verifier release on ClawHub](https://clawhub.ai/docsor1212/skills/pubmed-verifier)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and commands; verification reports in text, HTML, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional audit JSON and verified BibTeX; unreachable registries yield an unknown verdict rather than an invalid citation.]

## Skill Version(s):

2.7.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
