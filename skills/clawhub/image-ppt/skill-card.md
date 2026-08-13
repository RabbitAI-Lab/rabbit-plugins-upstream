## Description:

Image PPT turns books, PDFs, and other text materials into editable PPTX presentation decks through a three-step workflow for content extraction, image-based slide generation, and editable slide reconstruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloo1568](https://clawhub.ai/user/helloo1568)

### License/Terms of Use:

MIT

## Use Case:

External users, students, educators, researchers, and presentation authors use this skill to convert books, papers, reports, PDFs, Markdown, or other source text into presentation decks for classes, book sharing, lab meetings, project reports, and pitch events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source documents, templates, or derived prompts may include confidential PDFs, unpublished research, student data, business reports, or proprietary material.

Mitigation: Use non-sensitive or redacted inputs unless the user accepts sending that content to the AI or image-generation provider used for the workflow.

Risk: The workflow can depend on cloud or external image-generation tools, creating privacy and network exposure not fully emphasized by the artifact documentation.

Mitigation: Confirm the selected provider and data-handling posture before use, and avoid uploading sensitive source material to providers that are not approved for the data.

Risk: Broad PPT-related trigger phrases could invoke the workflow unintentionally.

Mitigation: Invoke the skill explicitly for intended document-to-PPT tasks and confirm the workflow before processing user materials.

Risk: Image-generated and reconstructed slides may contain wrong text, missed details, font substitutions, or visually approximate charts.

Mitigation: Review generated previews and final PPTX output page by page, compare against source material, and disclose any font substitutions, retained image text, or approximate chart data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/helloo1568/skills/image-ppt)
- [Server-resolved GitHub repository](https://github.com/helloo1568/image-ppt)
- [Core prompts](references/prompts.md)
- [English README](README.en.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Files]

**Output Format:** [Markdown guidance with prompt text, optional shell or Python snippets, generated images, and PPTX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include style preview images, image-based PPTX decks, editable PPTX decks, rendered comparison previews, and delivery notes about editable text, embedded images, font substitutions, or visual approximations.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
