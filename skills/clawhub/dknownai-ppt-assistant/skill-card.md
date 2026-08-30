## Description:

深知可信PPT guides an agent through creating editable PowerPoint presentations from a topic or source materials, using dknowc Trusted Search for evidence-backed content when configured and producing provenance reports alongside the deck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to create business, government, training, and reporting presentations as editable .pptx files. It is especially suited to decks that need structured content planning, user confirmation gates, authoritative-source search, and clickable provenance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through phone verification, account/API-key creation, and optional credential persistence.

Mitigation: Require explicit user consent before initiating the vendor flow, do not display full secrets, and prefer a managed secret store or session-only environment variable over shell profile persistence.

Risk: Search terms may be sent to dknowc services when authoritative-source retrieval is used.

Mitigation: Avoid sensitive internal materials unless the user's organization permits this service; use material-only mode when search is not required or not approved.

Risk: Untrusted PPTX, media, or animation inputs may carry content or parser risks.

Mitigation: Review and scan user-supplied files before processing, keep generated work in an isolated project workspace, and avoid processing files from untrusted sources.

Risk: The security verdict requires review before installation.

Mitigation: Perform install-time review and scanning, with particular attention to credential handling, external service calls, and local writes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dknownai/skills/dknownai-ppt-assistant)
- [Generate Presentation Workflow](artifact/workflows/generate-pptx.md)
- [Routing Rules](artifact/workflows/routing.md)
- [SVG Authoring Contract](artifact/references/svg-authoring.md)
- [Material Usage and Provenance Rules](artifact/references/material_usage.md)
- [Style Presets](artifact/references/style-presets.md)
- [Content Pack Specification](artifact/references/content-pack.md)
- [Third-Party Component Notices](artifact/THIRD_PARTY_NOTICES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, configuration steps, constrained SVG/page code, editable .pptx files, and HTML provenance reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write project workspaces, search-result intermediates, SVG pages, validation reports, PowerPoint exports, and provenance HTML when used by an agent.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
