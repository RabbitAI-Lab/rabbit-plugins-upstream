## Description:

Merge an account revision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, or account operations agents use this skill for routine account maintenance when they need to merge an account revision from supplied merge guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process account-related data supplied in the prompt.

Mitigation: Provide only the account revision details needed for the merge task and avoid including credentials or unrelated sensitive data.

Risk: A merge result could incorrectly change or omit account fields if the supplied guidance is ambiguous.

Mitigation: Review merged_record, changed_fields, and preserved_fields before applying the result to any account system.

## Reference(s):

- [Account Merge Workbench on ClawHub](https://clawhub.ai/wxt-ai/skills/revision-handling-guidance-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise text or Markdown containing a merge_result object with merged_record, changed_fields, and preserved_fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only the merge guidance supplied in the current request and does not require credentials, private files, external systems, scripts, or persistence.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
