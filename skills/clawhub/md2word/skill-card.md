## Description:

Converts Markdown documents into professionally formatted Word documents for Chinese-language reports, legal documents, service proposals, papers, and work materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and developers use this skill to convert Markdown drafts into styled .docx files with presets, templates, tables, images, code blocks, footnotes, and configurable document formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Markdown with external image URLs can trigger outbound HTTP/HTTPS requests, which may expose network metadata or reach unintended internal resources.

Mitigation: Convert trusted Markdown only, or run the skill with restricted network egress when processing third-party content.

Risk: Markdown can cause reachable local image files to be embedded in the generated Word document.

Mitigation: Run conversions in a constrained working directory and review source Markdown paths before processing sensitive material.

Risk: Mermaid and SVG rendering can invoke local external tools on document-derived content.

Mitigation: Use sandboxing for untrusted inputs, keep rendering tools patched, and disable optional renderers where they are not needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cat-xierluo/skills/md2word)
- [ClawHub Publisher Profile](https://clawhub.ai/user/cat-xierluo)
- [Legal Skills Homepage](https://github.com/cat-xierluo/legal-skills)
- [Configuration Reference](references/config-reference.md)
- [Style Mappings](references/style-mappings.md)
- [Usage Examples](references/examples.md)
- [Configuration Template](assets/config-template.yaml)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated .docx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Word documents and reusable YAML configuration; may embed local or external images when converting Markdown.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
