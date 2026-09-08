## Description:

dknowc PPT assistant helps agents create editable PowerPoint presentations from user topics or materials by combining dknowc trusted search, source-linked content planning, constrained SVG authoring, and deterministic SVG-to-DrawingML compilation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Business, government, education, and presentation users can use this skill to turn topics, reports, notes, or supplied materials into editable .pptx decks with structured page plans and source-linked provenance reports. Agent developers can also use its workflows and scripts to validate constrained SVG pages and compile them into native PowerPoint objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Phone-based onboarding can create or retrieve a long-lived access key.

Mitigation: Use a pre-provisioned secret when possible, avoid requesting a new key unless needed, and persist the key only after explicit user intent.

Risk: Trusted search sends search terms to dknowc services.

Mitigation: Review search terms before execution and avoid including confidential or unnecessary personal data in queries.

Risk: The skill writes project, report, export, and backup files locally.

Mitigation: Review output locations and delete project backups or intermediate files when working with confidential materials.

Risk: Phone-based onboarding is not plainly disclosed to users at runtime.

Mitigation: Ensure users understand the verification step, service provider, and key persistence choice before onboarding.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dylanzhangzx/skills/dknowc-ppt-assistant)
- [README](README.md)
- [Generate PPTX Workflow](workflows/generate-pptx.md)
- [Routing Workflow](workflows/routing.md)
- [Content Pack Reference](references/content-pack.md)
- [Material Usage and Provenance Report Rules](references/material_usage.md)
- [SVG Authoring Contract](references/svg-authoring.md)
- [Style Presets](references/style-presets.md)
- [Third-Party Notices](THIRD_PARTY_NOTICES.md)
- [dknowc Open Service](https://open.dknowc.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands; generated artifacts include editable .pptx files, HTML provenance reports, constrained SVG pages, JSON search records, and local project files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DKNOWC_API_KEY for trusted search when source retrieval is required; writes project, report, preview, and export files locally.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
