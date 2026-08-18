## Description:

Searches public scholarly literature, normalizes cross-source bibliographic records into a deduplicated evidence base, and produces traceable clinical-trial literature and qualitative safety reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

External clinical-trial, medical, regulatory, and research users use this skill to search public literature about a drug, disease, method, or safety question and generate a traceable evidence base for background research, protocol planning, CSR support, or qualitative safety review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search topics and filters are sent to public bibliographic APIs during retrieval.

Mitigation: Use the skill only for public or non-confidential literature questions and avoid entering confidential research or subject data.

Risk: API keys can be exposed if pasted into chat or committed into shared files.

Mitigation: Configure keys through an environment variable or a manually edited local .env file, and do not include real keys in prompts, documentation, or reports.

Risk: Reports produced with citation verification disabled may contain unresolved or preliminary references.

Mitigation: Keep citation verification enabled for normal use and treat any verification-disabled report as preliminary until checked against official sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [README](README.md)
- [Operating SOP](references/sop.md)
- [OpenAlex API key guide](references/openalex_key.md)
- [Language policy](references/language_policy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON evidence files, Markdown or HTML reports, Excel workbooks, BibTeX/RIS exports, and optional Obsidian or Zotero exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local report artifacts with source labels, citation-verification status, and evidence-log traceability.]

## Skill Version(s):

0.6.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
