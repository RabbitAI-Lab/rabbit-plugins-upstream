## Description:

Automates a supervised literature-harvesting workflow across CNKI, NCBI, Google Scholar, and Zotero, including PDF retrieval guidance, local linked-file attachments, tags, and Chinese notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoge6666](https://clawhub.ai/user/xiaoge6666)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, research assistants, and developers use this skill to collect topic-focused literature from multiple sources and organize it into a Zotero collection with parent items, local linked PDFs, tags, and notes. It is intended for supervised workflows where the user verifies source access rights and credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated retrieval steps include anti-bot and proof-of-work bypass procedures.

Mitigation: Remove or disable those procedures and prefer official APIs, open-access bulk mechanisms, and user-mediated downloads when automation is blocked.

Risk: The workflow uses Zotero and NCBI credentials.

Mitigation: Provide only scoped credentials, avoid hardcoding secrets in reusable templates, and supervise each run.

Risk: Downloaded literature may be subject to institutional access rules or source-site terms.

Mitigation: Verify that each download is authorized by the user's institution and the source site before saving or importing files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoge6666/skills/literature-harvest-zotero)
- [CNKI](https://www.cnki.net/)
- [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/)
- [Europe PMC PDF render endpoint](https://europepmc.org/articles/{PMCID}?pdf=render)
- [Europe PMC full-text PDF endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextPDF)
- [PMC article PDF endpoint](https://pmc.ncbi.nlm.nih.gov/articles/{PMCID}/pdf/main.pdf)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions with Python script templates and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied Zotero and NCBI credentials, local browser access, source-site authorization, and Zotero linked-file configuration.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
