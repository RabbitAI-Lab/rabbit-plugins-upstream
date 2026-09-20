## Description:

Create editable PPTX from current reference images, articles, data, or a user template using model-authored content contracts, declarative design records, native object rendering, previews, and verification gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillmelody](https://clawhub.ai/user/skillmelody)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, consultants, and content teams use this skill to convert long-form sources, reference images, data, and approved templates into editable presentation decks with explicit content, design, rendering, and QA evidence. It is intended for source-to-deck and template-preserving workflows where final delivery requires reviewable PPTX output rather than a flat screenshot or unchecked draft.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may execute local Python, Node, and office-rendering tools while building or verifying decks.

Mitigation: Run it in an isolated workspace, review scripts before execution, and use copies of sensitive source documents, templates, and decks.

Risk: Some documented routes can rely on model- or user-authored code or refinement steps with broad local authority.

Mitigation: Prefer the declarative design route and fixed renderer where possible, and require human review before executing author/refine scripts.

Risk: Cloud slide export or upload could expose presentation content outside the local environment.

Mitigation: Confirm explicitly before any cloud export or Feishu Slides routing, and avoid uploading sensitive material unless authorized.

Risk: A generated PPTX can be incomplete, visually incorrect, or less editable than claimed if rendering and readback are unavailable.

Mitigation: Use the documented status model and verification gates; do not treat a deck as final unless real rendering, structural inspection, and required review records pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt)
- [Declarative design workflow](artifact/references/declarative-design.md)
- [V4 template route](artifact/docs/v4-template-route.md)
- [Three-route architecture](artifact/docs/v4-three-route-architecture.md)
- [Production readiness gates](artifact/references/production-readiness-gates.md)
- [Verification harness contract](artifact/references/verification-harness.md)
- [python-pptx native objects API](https://python-pptx.readthedocs.io/en/latest/api/shapes.html)
- [LibreOffice command-line conversion parameters](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON contracts, shell commands, generated PPTX files, QA reports, previews, and delivery manifests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces editable presentation artifacts when required dependencies and review gates are available; final status should distinguish planned, created, rendered, read_back, verified, final, and failed states.]

## Skill Version(s):

5.0.0-alpha.1 (source: SKILL.md frontmatter, README.en.md, VERSION, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
