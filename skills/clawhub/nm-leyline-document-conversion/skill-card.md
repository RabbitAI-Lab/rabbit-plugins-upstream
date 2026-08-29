## Description:

Converts documents and URLs to markdown via tiered fallback through MCP markitdown, native tools, and user notice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert PDFs, Office documents, web pages, images, data files, and other document inputs into markdown for downstream processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local files and remote URLs provided for conversion may contain confidential or private content.

Mitigation: Only provide files and URLs that the configured conversion tools are allowed to read or fetch.

Risk: Optional MCP setup can expand the environment's document conversion behavior.

Mitigation: Review the markitdown MCP configuration before adding it to the agent environment.

Risk: Converted external content may contain instructions that should not control the agent.

Mitigation: Apply the skill's content-sanitization checklist, including truncation, stripping instruction tags, and boundary markers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-document-conversion)
- [ClawHub publisher profile](https://clawhub.ai/user/athola)
- [Homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [Format support matrix](modules/format-matrix.md)
- [Fallback tier instructions](modules/fallback-tiers.md)
- [URI construction rules](modules/uri-construction.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with setup snippets and conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Converted content should be treated as external input and sanitized before downstream use.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
