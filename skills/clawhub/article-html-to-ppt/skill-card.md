## Description:

Creates editable presentations from source documents, reconstructs supplied slide designs, or reuses native PPTX templates with rendered previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillmelody](https://clawhub.ai/user/skillmelody)

### License/Terms of Use:

Apache-2.0

## Use Case:

Presentation creators and developers use this skill to turn documents into editable slide decks, rebuild supplied designs, or populate native templates while checking content and rendered previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advanced authoring or refinement routes can run local Python scripts with the agent's privileges.

Mitigation: Prefer the declarative workflow; review scripts before running advanced routes in an isolated environment without sensitive credentials.

Risk: Local PPT generation can invoke Office or LibreOffice on supplied content.

Mitigation: Install and run only when local document processing is acceptable; review the generated presentation before delivery.

## Reference(s):

- [MeowClaw PPT Smith release](https://clawhub.ai/skillmelody/skills/article-html-to-ppt)
- [python-pptx shape documentation](https://python-pptx.readthedocs.io/en/latest/api/shapes.html)
- [LibreOffice command-line conversion documentation](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [Editable PPTX, rendered slide previews, and review or delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Native slide objects where supported; disclose material editing limitations and raster exceptions.]

## Skill Version(s):

5.2.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
