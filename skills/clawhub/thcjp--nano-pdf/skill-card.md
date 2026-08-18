## Description:

PDF精简工具 helps agents use the nano-pdf CLI to edit and manage PDF files from natural-language instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, document operators, and agent users use this skill to generate guidance and commands for PDF extraction, conversion, editing, merging, compression, and related file-management workflows through nano-pdf.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run PDF-editing CLI commands against local files.

Mitigation: Use copies of PDFs, require explicit output paths, and review each command before execution.

Risk: The security summary flags mixed PDF-editing, workflow orchestration, and external API language.

Mitigation: Review the skill instructions before installation and limit use to trusted documents and controlled workspaces.

Risk: Sensitive PDFs could be exposed if processing behavior is not understood.

Mitigation: Avoid sensitive documents unless the operator has confirmed whether nano-pdf processes data locally or externally.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can ask an agent to read, execute commands, and write files when handling local PDFs.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
