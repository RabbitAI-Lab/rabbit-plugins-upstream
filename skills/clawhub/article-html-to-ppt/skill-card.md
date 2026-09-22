## Description:

Creates editable PPTX presentations from documents, supplied slide designs, or native PPTX templates with structured native objects and real rendered previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillmelody](https://clawhub.ai/user/skillmelody)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and presentation-building agents use this skill to turn source documents, full-slide design references, or PPTX templates into editable, evidence-backed decks with previews, speaker notes, and delivery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advanced routes can run user- or model-authored Python with broad local privileges.

Mitigation: Prefer the declarative create/recreate workflow for normal use, and run Bespoke, refine, or model-authored component routes in a sandboxed or disposable workspace.

Risk: Local renderers and author scripts may access or write local paths during PPT production.

Mitigation: Review script and output paths before execution and install only where this local execution posture is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt)
- [README.en.md](README.en.md)
- [Skill entry point](SKILL.md)
- [Declarative workflow](references/declarative-design.md)
- [Template workflow](references/routes/v4-template-route.md)
- [v5.1 sample evidence](assets/samples/v5.1-no-image-policy-evidence.json)

## Skill Output:

**Output Type(s):** [files, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus editable PPTX files, rendered previews, JSON evidence reports, and command-line build or verification steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces final delivery only after route-specific rendering, review, and edit/save/reopen checks; advanced routes may involve local renderers or Python author scripts.]

## Skill Version(s):

5.1.0 (source: server release metadata, SKILL.md frontmatter, README.en.md, VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
