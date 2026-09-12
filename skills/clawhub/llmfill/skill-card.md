## Description:

AI Word Form Filling helps an agent upload .docx forms, questionnaires, checklists, and reference materials to LLMFill so the remote service can generate and download completed Word documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[viverglow](https://clawhub.ai/user/viverglow)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to fill Word forms and questionnaires from uploaded templates, reference documents, knowledge bases, or web-backed answer sources. It is suited to DDQs, compliance questionnaires, applications, surveys, and batch form completion when the user approves remote processing by LLMFill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected Word forms, reference documents, and knowledge-base files are sent to LLMFill for remote processing.

Mitigation: Use the skill only after confirming the user is authorized to share the documents; redact or avoid confidential, regulated, personal, and internal-only content unless remote processing has been approved.

Risk: The skill relies on a long-lived LLMFill API key stored in local configuration.

Mitigation: Have the user configure the key directly, keep it out of chat and command history, protect ~/.llmfill/config.json, and revoke or recreate the key if exposure is suspected.

Risk: AI-filled form answers may be incomplete or incorrect.

Mitigation: Review generated Word documents before relying on them for business, compliance, legal, or submission workflows.

Risk: Knowledge-base and result cleanup operations can remove server-side files or outputs.

Mitigation: Confirm the target IDs before deletion and download any needed originals or completed results first.

## Reference(s):

- [LLMFill skill README](README.md)
- [Document filling API](references/api-documents.md)
- [Knowledge base API](references/api-knowledge.md)
- [Account and configuration](references/api-account.md)
- [curl guide](references/curl-guide.md)
- [Error code reference](references/errors.md)
- [Skill page](https://clawhub.ai/viverglow/skills/llmfill)
- [Publisher profile](https://clawhub.ai/user/viverglow)
- [LLMFill service](https://www.llmfill.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with shell commands, optional JSON CLI output, and downloaded Word document files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The fill workflow can download processed and clean .docx outputs; account, status, and knowledge-base commands can emit machine-readable JSON.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence and README version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
