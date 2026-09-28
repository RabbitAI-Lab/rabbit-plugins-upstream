## Description:

Helps agents create, read, and edit PowerPoint presentations, with optional image generation and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing presentations use this skill to create editable slide decks, work with existing PPTX files, and optionally add imagery or review slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The LibreOffice helper can load native code from a shared temporary path.

Mitigation: Fix or disable the helper in shared environments; use a controlled workspace and a reviewed, pinned release.

Risk: Optional QA broadly delegates work, and optional image generation invokes additional tools.

Mitigation: Enable QA and image generation only when their extra tools are appropriate; review sensitive presentations before using them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mebusw/skills/jackyshen-gen-pptx)
- [Server-resolved source repository](https://github.com/mebusw/jackyshen-gen-pptx)
- [PptxGenJS documentation](https://pptxgen.js.org/)
- [Slide layout reference](references/slide-layouts.md)
- [Diagram reference](references/diagrams.md)
- [UPerform brand palette](references/优普丰品牌设计配色方案.md)

## Skill Output:

**Output Type(s):** [Code, Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and JavaScript code for editable PPTX presentations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default generates PPTX only; image generation and QA require explicit options.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
