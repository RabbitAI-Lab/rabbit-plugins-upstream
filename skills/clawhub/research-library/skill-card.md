## Description: <br>
Local-first multimedia research library for hardware projects. Capture code, CAD, PDFs, images. Search with material-type weighting. Project isolation with cross-references. Async extraction. Backup + restore. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonbuckles](https://clawhub.ai/user/jonbuckles) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and hardware project teams use this skill to organize local project materials, extract searchable content, find prior work, link related documents, and export research records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Imported files, downloaded materials, extracted text, image metadata, indexes, exports, and backups may contain sensitive local research data. <br>
Mitigation: Use trusted inputs, avoid importing sensitive photos when EXIF retention is not acceptable, review export destinations, and apply local access controls to the research library and backup directories. <br>
Risk: Bulk imports, restore operations, and automated extraction can change or replace local library state. <br>
Mitigation: Create a fresh backup before restore or bulk import workflows, verify selected backup dates, and test high-volume imports on non-critical data first. <br>
Risk: OCR and parser quality varies by document type and image clarity, which can make search results incomplete or misleading. <br>
Mitigation: Review extracted content and confidence scores for important materials, and keep source files available for manual verification. <br>


## Reference(s): <br>
- [ClawHub Research Library listing](https://clawhub.ai/jonbuckles/skills/research-library) <br>
- [CLI Reference](docs/CLI-REFERENCE.md) <br>
- [Extraction Guide](docs/EXTRACTION-GUIDE.md) <br>
- [Search Guide](docs/SEARCH-GUIDE.md) <br>
- [Worker Guide](docs/WORKER-GUIDE.md) <br>
- [Technical Notes](TECHNICAL-NOTES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce JSON or Markdown exports when using the library's export commands.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
