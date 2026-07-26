## Description: <br>
Converts documents and URLs to markdown through tiered fallback using MCP markitdown, native tools, or user guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert PDFs, Office documents, web pages, data files, images, audio, archives, and e-books into markdown for downstream workflows. It helps agents choose an available conversion path, sanitize external content, and clearly report when extra tooling is required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents and URLs may contain sensitive or untrusted external content. <br>
Mitigation: Review files and URLs before processing, then apply the documented sanitization steps before using converted content downstream. <br>
Risk: The optional markitdown MCP server or related plugin adds external conversion tooling to the agent environment. <br>
Mitigation: Enable that tooling only when trusted and needed; otherwise rely on native fallbacks or ask the user to provide a supported format. <br>


## Reference(s): <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Format support matrix](modules/format-matrix.md) <br>
- [Fallback tier instructions](modules/fallback-tiers.md) <br>
- [URI construction rules](modules/uri-construction.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with inline configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Converted external content should be sanitized, bounded, and reviewed before downstream use.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
