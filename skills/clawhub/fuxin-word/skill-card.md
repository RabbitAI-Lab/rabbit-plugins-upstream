## Description:

福昕 Office 文档助编 helps an agent edit the active Fuxin Office Word document by using Word scene tools for report generation, terminology cleanup, highlighting and comments, and checklist review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document authors use this skill to let an agent perform structured Word document workflows in Fuxin Office, including writing reports, standardizing terminology and formatting, adding highlights or comments, and creating checklist review output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change the currently open Fuxin Office Word document.

Mitigation: Use it only for intended document-editing workflows, review the document after changes, and rely on the documented undo or save-cancel prompts when output is not intended.

Risk: A write workflow may run against the wrong or unprepared Word session if prerequisites are not checked.

Mitigation: Run the documented prechecks before write actions and proceed only when FuxinAiService, the Word product, and an active document are ready.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-word)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON tool-call parameters and user-facing completion text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running FuxinAiService, a registered Word product, and an active Word document before write workflows are executed.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
