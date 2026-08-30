## Description:

Docxport helps agents convert Markdown, HWP, DOCX, RTF, and Marp slide files into PDF, PNG, HTML, DOCX, or PPTX outputs using documented converter priorities and fallback rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose appropriate document conversion workflows, preserve rich formatting for document analysis, and avoid watermarked outputs for external deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or overwrite output files during document conversion.

Mitigation: Run it first in a project directory with non-sensitive test files and review output paths before sharing results.

Risk: The skill may use npx to fetch and execute Marp tooling.

Mitigation: Preinstall trusted converter versions where possible and verify tool versions before use.

Risk: Generated Mermaid HTML can load remote JavaScript from jsDelivr when opened.

Mitigation: Review generated HTML before sharing or opening it in sensitive environments.

## Reference(s):

- [Docxport on ClawHub](https://clawhub.ai/drumrobot/skills/docxport)
- [docx.md](artifact/docx.md)
- [marp.md](artifact/marp.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and generated document file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PDF, PNG, HTML, DOCX, or PPTX files depending on the requested conversion path.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
