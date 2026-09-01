## Description:

福昕 Office 助手 routes Office requests across Word, Excel, and PowerPoint for preflight checks, document editing, read-only document Q&A, batch undo guidance, and cross-product workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

Proprietary

## Use Case:

Fuxin Office users use this skill to ask an agent, in Simplified Chinese, to inspect readiness and perform guided Word, Excel, and PowerPoint tasks such as report writing, data extraction, chart creation, presentation generation, document Q&A, and grouped undo workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify active Word, Excel, and PowerPoint documents after user-directed write requests.

Mitigation: Run the documented preflight and window checks, keep the intended document active, and use the documented Ctrl+Z or reply-based undo guidance when a normal write needs to be reverted.

Risk: Save operations are not reversible through undo.

Mitigation: Require the documented save confirmation before calling save_document or save_document_as, and do not save when the user cancels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-office)
- [README](README.md)
- [Input schema](schema/input_schema.json)
- [Sample case](examples/sample_case.json)
- [fuxin-office-bridge connection and preflight reference](reference/bridge.md)
- [fuxin-word document orchestration reference](reference/word.md)
- [fuxin-excel spreadsheet orchestration reference](reference/excel.md)
- [fuxin-ppt presentation orchestration reference](reference/ppt.md)
- [fuxin-doc-qa document Q&A reference](reference/doc-qa.md)
- [fuxin-batch-undo batch undo reference](reference/batch-undo.md)
- [fuxin-custom-tool custom workflow example](reference/custom-tool.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text instructions with structured tool parameters when document operations are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are intended for Simplified Chinese user interactions and may include preflight status, operation summaries, save confirmations, and undo guidance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
