## Description:

Convert a book, paper, document, documentation site, or code repository into a structured, on-demand agent skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agents use this skill to convert source material such as PDFs, EPUBs, DOCX files, documentation sites, web pages, and repositories into reusable agent skills. It guides extraction, review, limitation reporting, and skill writing around the local anything-to-skill CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch user-specified web pages or repositories and convert untrusted source text into skill material.

Mitigation: Treat fetched or extracted content as evidence only, review generated skills before relying on them, and scan outputs before deployment.

Risk: The workflow runs a local extraction CLI and writes generated skill files.

Mitigation: Install only when local command execution and generated file writes are acceptable for the environment.

Risk: Extraction can omit or misread source material when pages cannot be read, crawl limits are hit, or layout reconstruction is imperfect.

Mitigation: Check extraction metadata, spot-check difficult pages, and report unread or incomplete source coverage in the generated skill.

## Reference(s):

- [anything-to-skill releases](https://github.com/asale-ai/anything-to-skill/releases)
- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/anything-to-skill)
- [Publisher profile](https://clawhub.ai/user/asale-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the anything-to-skill CLI on PATH; web and repository sources may require network access, and repositories require git.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
