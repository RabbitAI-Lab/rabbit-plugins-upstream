## Description: <br>
Converts documents and URLs to markdown via tiered fallback using MCP markitdown, native tools, and user notice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to convert PDFs, Office documents, web pages, structured data files, images, audio, archives, and e-books into markdown for downstream agent workflows. It is intended as shared document-ingestion infrastructure for skills that need external content in markdown form. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local files or URLs may expose their content to the configured markitdown MCP server or native fetch/read tools. <br>
Mitigation: Review the configured conversion tools and only convert files or URLs that are appropriate to share with those tools. <br>
Risk: Broad conversion-related triggers may activate the skill during general document-conversion discussions. <br>
Mitigation: Confirm that the user is asking to convert or ingest non-plain-text content before applying the conversion protocol. <br>
Risk: Some formats have limited native fallback support and may produce incomplete or lower-fidelity markdown without markitdown. <br>
Mitigation: Use the documented tiered fallback path, disclose limitations for unsupported formats, and avoid guessing content that cannot be read. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-document-conversion) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Format support matrix](artifact/modules/format-matrix.md) <br>
- [Fallback tier instructions](artifact/modules/fallback-tiers.md) <br>
- [URI construction rules](artifact/modules/uri-construction.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline JSON and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Converted content should be sanitized as external content; conversion quality depends on file format and available tooling.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
