## Description:

Create an access review checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Collaboration and operations users use this skill to turn workspace membership changes into a concise access-review checklist for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace membership details may include names, roles, or external-entry information.

Mitigation: Provide only the membership details needed for the checklist and avoid including unrelated personal or sensitive information.

Risk: The checklist depends on the accuracy and completeness of the supplied access_delta.

Mitigation: Review the generated checklist against the source membership changes before using it for access-review follow-up.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/workspace-access-checklist-workbench)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Structured checklist artifact with checklist_id, workspace_id, and items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user-supplied access_delta object and does not require credentials, private files, commands, network access, or persistence.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
