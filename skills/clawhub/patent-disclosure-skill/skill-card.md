## Description:

China patents skill for mining patent points, drafting invention, utility-model, and design disclosures, reading patents in plain language, monitoring policy signals, and assisting with office-action responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, inventors, and patent practitioners use this skill to turn project materials, patent numbers, PDFs, and office-action materials into China patent disclosure drafts, plain-language patent notes, prior-art search summaries, policy review backlogs, and review-ready office-action response drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local project-document access, command execution, and writes to output, Obsidian, and office-action data directories.

Mitigation: Install and run it only in workspaces where those permissions are acceptable, and keep sensitive projects isolated from unrelated local files.

Risk: Mode D can automatically use a third-party book-to-skill helper.

Mitigation: Review and pin that helper before use, or install a manually reviewed version instead of accepting an automatic install path.

Risk: Embedding credentials may be stored in plaintext configuration.

Mitigation: Prefer environment variables or a protected secret store, and avoid passing API keys on command lines.

Risk: Document parsers, browser automation, and optional CAD tooling increase dependency and file-processing exposure.

Mitigation: Pin dependencies for production use and process untrusted Office, PDF, and CAD inputs inside a sandbox.

Risk: Office-action response outputs are drafts that could be legally consequential if filed without review.

Mitigation: Require qualified human review before submitting any generated response or disclosure material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill)
- [Publisher profile](https://clawhub.ai/user/handsomestwei)
- [README](artifact/README.md)
- [Installation guide](artifact/INSTALL.md)
- [Patent domain rules](artifact/references/patent_domain_rules.yaml)
- [Patent type search rules](artifact/references/patent_type_search.yaml)
- [Patent PDF sources](artifact/references/patent_pdf_sources.yaml)
- [Patent Obsidian format](artifact/references/patent_obsidian_format.md)
- [Schema reference index](artifact/references/schemas/README.md)
- [Patent reader tooling](artifact/tools/patent_reader/README.md)
- [Office-action tooling](artifact/tools/oa/README.md)
- [book-to-skill helper](https://github.com/virgiliojr94/book-to-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, DOCX, YAML, JSON, SVG/PNG diagrams, shell commands, and configuration files depending on the workflow mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can be written to timestamped disclosure folders, Obsidian vaults, office-action data directories, or evolution backlog files; office-action drafts require human review before filing.]

## Skill Version(s):

3.9.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
