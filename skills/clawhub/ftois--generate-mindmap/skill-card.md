## Description:

Generates cognitive-science-grounded interactive mind maps from Markdown outlines or JSON, with exports to HTML, PNG, JPG, SVG, PDF, and XMind plus a structure quality report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ftois](https://clawhub.ai/user/ftois)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and knowledge workers use this skill to turn articles, notes, meeting summaries, learning material, and structured outlines into editable mind maps and shareable exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML may execute injected script content from untrusted outlines.

Mitigation: Use trusted source content, or avoid HTML/PNG/JPG rendering for untrusted outlines until the escaping issue is fixed.

Risk: The skill can automatically install Pillow into the current Python environment.

Mitigation: Use --no-auto-install in shared or sensitive environments and install dependencies manually in an isolated environment.

Risk: The generated HTML save button can enable Chrome or Edge autosave back to the selected file.

Mitigation: Only bind autosave to files you intend the browser to update, and review browser prompts before granting file access.

## Reference(s):

- [Generate Mindmap on ClawHub](https://clawhub.ai/ftois/skills/generate-mindmap)
- [Mind Map Content Design Methodology](artifact/references/methodology.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that produce HTML, PNG, JPG, SVG, PDF, XMind, and quality-report text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; Pillow is required for PNG/JPG/PDF export and may be installed automatically unless --no-auto-install is used.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
