## Description:

Create editable PPTX from documents, reconstruct supplied slide design images, or preserve native PPTX templates with structured native objects and real previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillmelody](https://clawhub.ai/user/skillmelody)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn source documents, slide design references, or native PPTX templates into editable presentations with previews, speaker notes, source evidence, and delivery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advanced routes can run model- or caller-supplied Python with broad local file and environment access.

Mitigation: Use the default declarative workflow for ordinary decks and invoke Bespoke, refine-code, or model-authored template component routes only with trusted Python scripts.

Risk: The skill runs local PPT-generation and rendering tools and writes task artifacts.

Mitigation: Install and run it only in an environment where LibreOffice/Poppler execution and local artifact writes are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt)
- [Publisher profile](https://clawhub.ai/user/skillmelody)
- [Declarative workflow](artifact/references/declarative-design.md)
- [Template visual design](artifact/references/template-visual-design.md)
- [Verification harness](artifact/references/verification-harness.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Editable PPTX files, rendered previews, speaker notes, QA reports, and concise delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write task artifacts and may use local office/rendering tools when producing or verifying decks.]

## Skill Version(s):

5.1.1 (source: server release, frontmatter, VERSION, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
