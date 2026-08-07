## Description:

Origin Office helps agents convert native DOCX and PPTX files into verifiable structured packages with anchored document objects, expanded tables, slide structures, SHA-256 structure fingerprints, and verification commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-automation teams use this skill to inspect or import native Office documents into verifiable structured packages for AI anchoring, document version tracking, and clause-level citation. It is most relevant when source DOCX or PPTX structure should be preserved instead of inferred from scanned PDFs or OCR output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks users to clone and run an external repository before processing Office documents.

Mitigation: Review the external repository source before cloning or running commands, and execute it only in an environment approved for the documents being processed.

Risk: Processing documents writes document structure and hashes into local output packages.

Mitigation: Run the CLI only on documents intended for local processing, and handle generated packages according to the applicable data retention and access-control requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/origin-office)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, configuration]

**Output Format:** [Markdown with inline shell commands and structured object descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local Node.js CLI use for DOCX/PPTX inspection, import, package verification, and Markdown or JSON export.]

## Skill Version(s):

1.0.1 (source: evidence.release.version; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
