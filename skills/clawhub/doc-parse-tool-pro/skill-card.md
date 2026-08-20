## Description:

Document parsing and OCR skill for extracting structured text, tables, and layout information from PDFs, images, and scanned documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation teams use this skill to parse PDFs, images, and scanned documents into structured text, tables, OCR output, and layout information for batch document workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad document read/write access and possible shell execution for parsing workflows.

Mitigation: Review the skill before installation, run it in a limited workspace, and grant file and command access only for documents and commands required by the task.

Risk: Sensitive document contents may be exposed through callbacks, webhooks, cloud OCR, or API-key backed integrations.

Mitigation: Do not enable callbacks, webhooks, cloud OCR, or API-key features for sensitive documents unless the data destination is confirmed and the user explicitly approves.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/doc-parse-tool-pro)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with Python, Bash, YAML, and JSON examples; parsed document results may be emitted as JSON, XML, CSV, or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read input documents, run local parsing commands, and write structured output files when the user grants the agent those capabilities.]

## Skill Version(s):

1.0.0 (source: server release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
