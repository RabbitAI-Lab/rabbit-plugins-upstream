## Description:

Convert a Markdown file into a mobile-friendly local HTML page or phone-sized screenshot. Safe default is local-only; a public web URL is only produced when the user explicitly asks for it or the host platform deploy tool is used. Respond in the user's current language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent users use this skill to convert Markdown files into mobile-friendly local HTML, phone-sized screenshots, or explicit-request public web output for easier review and sharing outside chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML can include local images, and broad local-image embedding can expose more local content than intended.

Mitigation: Keep the default image mode for untrusted documents and review image references before sharing generated HTML.

Risk: Public URL deployment can publish converted Markdown content beyond the local machine.

Mitigation: Request public URLs only when the content is intended to be published and a trusted deploy path is available.

Risk: Converted Markdown may contain misleading links or content from untrusted documents.

Mitigation: Review generated output before sharing or relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/md-out-of-chat)
- [Project homepage](https://github.com/bonniegeng-max/md-out-of-chat)
- [Live web demo](https://2uf0a7axwwwr.space.minimaxi.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands that produce local HTML files, phone-sized PNG screenshots when requested, or public URLs only on explicit request with a trusted deploy path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally by default with python3; remote images are not fetched automatically, and broad local-image embedding requires an explicit option.]

## Skill Version(s):

1.3.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
