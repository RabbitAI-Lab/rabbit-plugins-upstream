## Description:

KingDoc lets an agent create, edit, manage, compare, check, and recover Kingsoft/WPS online documents across document, spreadsheet, presentation, multidimensional table, form, visualization, history, and attachment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, document operators, and teams using WPS documents use KingDoc to let an agent create, edit, upload, download, search, recover, compare, and check documents through WPS APIs and local generation/OCR helpers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with broad WPS document authority and includes high-impact document actions.

Mitigation: Use a dedicated least-privilege WPS app and require a separate confirmation step before destructive, permission-changing, sharing, or bulk operations.

Risk: The App Secret may be stored in local configuration.

Mitigation: Protect config.json as a secret, avoid sharing it, and rotate the App Secret if exposure is suspected.

Risk: Template refresh, webhooks, share links, uploads, downloads, and generated HTML reports may expose sensitive content or destinations.

Mitigation: Review destinations, generated artifacts, and outbound links before use, and treat downloaded files and reports as sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/kingdoc)
- [Kingsoft Developer Platform](https://developer.kdocs.cn)
- [WPS Open Platform](https://open.wps.cn)
- [WPS AI PPT API documentation](https://open.wps.cn/documents/app-integration-dev/docs-center/aippt/Document)
- [WPS meeting minutes API documentation](https://open.wps.cn/documents/app-integration-dev/wps365/server/meeting/minutes/create_minute)
- [Security design](references/security.md)
- [Rate limits and hardware adaptation](references/rate_limit.md)
- [Office conversion and extraction references](references/office_references.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls]

**Output Format:** [Markdown and structured tool-call results, with generated document files or local reports when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify WPS documents, local DOCX/PPTX/SVG/HTML/JSON artifacts, OCR text, formulas, summaries, diffs, and configuration guidance.]

## Skill Version(s):

3.7.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
