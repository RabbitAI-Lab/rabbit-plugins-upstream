## Description:

Smart Classroom Teaching helps agents plan, generate, display, and review classroom instruction across teaching visualization, Socratic dialogue, classroom-record analysis, personalized instruction, multimodal command parsing, teaching-resource generation, and education safety checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, students, and education teams use this skill to turn natural-language teaching inputs into lesson plans, classroom visualizations, guided dialogue, diagnostic reports, differentiated instruction, reusable workbench timelines, and privacy-aware teaching resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local workbench can read and overwrite classroom state without authentication.

Mitigation: Run the workbench only in a trusted local environment, stop the helper server when not needed, and add authentication plus narrow CORS before sensitive classroom use.

Risk: Imported lesson JSON and rendered HTML/SVG content can introduce unsafe or misleading content.

Mitigation: Import only trusted lesson JSON, validate schema and size, sanitize HTML/SVG content, and review generated educational material before classroom use.

Risk: Real student personal data may be exposed through workbench state, imports, or exports.

Mitigation: Avoid putting real student personal data into the workbench unless the deployment is hardened, and apply privacy redaction before analysis, export, or sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wangjiaocheng/skills/smart-classroom-teaching)
- [Smart Classroom Task Catalog](references/smart-classroom-catalog.md)
- [Smart Classroom Requirements](references/smart-classroom-requirements.md)
- [Smart Classroom Exemplars](references/smart-classroom-exemplars.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON teaching-state snapshots, optional SVG/HTML snippets, and shell commands for the local workbench server]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce workbench state JSON for import/export or local POST updates; the local server is optional for real-time workbench updates.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
