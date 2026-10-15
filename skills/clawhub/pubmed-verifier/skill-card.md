## Description:

Checks cited PMIDs, DOIs, and arXiv IDs against academic registries and compares publication metadata with claimed references to flag mismatches, retractions, and unverified citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit reference lists and AI-generated citations before publication or use in a knowledge base. It compares claimed citation details with registry records and produces reviewable verification results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, and optional contact or API-key parameters are sent to academic registries.

Mitigation: Use the skill only when this disclosure is acceptable, and avoid submitting sensitive citation details or credentials unnecessarily.

Risk: Scanning broad directories may include unintended citation files, and reports or bundles may be written to unintended paths.

Mitigation: Choose narrow input files or directories and review output paths before generating reports or bundles.

Risk: The local SQLite cache may retain previous lookup results and make retraction or DOI information stale.

Mitigation: Use --no-cache when local retention is unwanted or for a fresh final citation check.

## Reference(s):

- [PubMed Verifier on ClawHub](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [API examples](references/api_examples.md)
- [Python API](references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, JSON]

**Output Format:** [Citation-verification guidance and commands; the verifier can write text, HTML, JSON, CSV, BibTeX, RIS, and formatted reference lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state verdicts with citation evidence; registry or network failures remain unverified rather than invalid.]

## Skill Version(s):

4.7.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
