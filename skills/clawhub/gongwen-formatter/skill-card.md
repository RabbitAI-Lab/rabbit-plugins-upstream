## Description:

Official Doc converts Markdown into Word documents formatted for the Chinese GB/T 9704-2012 government document standard, with optional remote image downloading that can be disabled.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edwardwason](https://clawhub.ai/user/edwardwason)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn Markdown reports, briefs, and other generated content into GB/T 9704-2012-style Word documents for review or distribution. It performs formatting conversion only and does not classify document type, add official document decorations, or review content compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote images in Markdown can trigger outbound requests to user-supplied http/https hosts when image downloading is enabled.

Mitigation: For untrusted Markdown or restricted networks, pass download_images=False or review image URLs before conversion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/gongwen-formatter)
- [Project homepage](https://github.com/EdwardWason/official-doc)
- [Project README](https://github.com/EdwardWason/official-doc/blob/main/README.md)
- [Project releases](https://github.com/EdwardWason/official-doc/releases)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [DOCX file plus a structured success/output_path status object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes the requested .docx output path; remote images may be embedded when download_images is enabled.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata, skill frontmatter, changelog, setup.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
