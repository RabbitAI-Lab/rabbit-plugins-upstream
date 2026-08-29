## Description:

深知可信PPT helps agents create editable PowerPoint presentations by researching authoritative source materials, drafting slide content, hand-authoring constrained SVG pages, and compiling them into native .pptx files with source-verification reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, public-sector teams, and business users use this skill to turn topics, working materials, reports, or meeting notes into editable presentations. It supports presentation planning, authoritative-material lookup when configured, source tracing, SVG-based slide authoring, quality checks, and native PowerPoint export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles phone verification and API-key onboarding for search access.

Mitigation: Review before installing, be comfortable providing a phone number and verification code to the provider, and avoid exposing full access keys in conversation or shared files.

Risk: Generated presentations and local outputs may include confidential or sensitive source material.

Mitigation: Avoid sensitive decks until output-file permissions and sharing behavior are reviewed for the target environment.

Risk: Endpoint scope and sharing behavior are under-disclosed in the security evidence.

Mitigation: Review the declared network endpoints and local write paths before use, especially on shared machines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-ppt-assistant)
- [dylanzhangzx publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [Generate PPTX workflow](workflows/generate-pptx.md)
- [Routing workflow](workflows/routing.md)
- [Constrained SVG authoring contract](references/svg-authoring.md)
- [Material usage and source-verification rules](references/material_usage.md)
- [Content pack specification](references/content-pack.md)
- [Style presets](references/style-presets.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)
- [dknowc search API endpoint](https://open.dknowc.cn/)
- [dknowc platform](https://platform.dknowc.cn/)
- [ppt-master upstream project](https://github.com/hugohe3/ppt-master)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands, project files, constrained SVG, HTML source-verification reports, and native .pptx exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local project workspaces, intermediate search records, validation reports, and editable PowerPoint deliverables.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
