## Description:

福昕 Office 企业工具 demonstrates how enterprises can combine existing Fuxin Office Word scenario tools into reusable custom document workflows such as contract review, terminology unification, highlighting, comments, checklist review, and report generation.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and enterprise workflow builders use this skill to turn repeated Fuxin Office Word document operations into reusable, one-command workflows. The documented examples focus on contract review, report generation with self-checking, terminology normalization, and checklist-based document review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or generate Word documents through existing Fuxin Office workflows.

Mitigation: Use it only with the intended Fuxin Office document workflow stack, confirm the active document before running document-editing workflows, and review the resulting changes.

Risk: Broad trigger phrases such as "custom tool" or "自定义" may invoke document-editing workflows unexpectedly.

Mitigation: Narrow or customize trigger phrases before deployment so routine requests do not start document-editing workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-custom-tool)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured workflow steps and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for invoking existing Fuxin Office Word tools; it does not add new gateway tools.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
