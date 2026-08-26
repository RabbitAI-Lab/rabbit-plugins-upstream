## Description:

AI project management powered by CellCog. Knowledge workspaces, document upload, AI-processed context trees, signed URL retrieval. Works standalone or as CellCog chat context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to create CellCog project workspaces, upload documents, inspect AI-processed context trees, and retrieve signed document URLs for project-based workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded documents are processed by a remote project and document service, which can expose confidential or regulated data if used without permission.

Mitigation: Use the skill only when CellCog is an intended service for the workflow, and upload confidential, regulated, or third-party files only with authorization.

Risk: Signed URLs provide temporary document access to anyone who has the link until the URL expires.

Mitigation: Treat signed URLs as temporary secrets, share them only with intended recipients, and use the shortest practical expiration window.

Risk: The skill requires a CELLCOG_API_KEY for authenticated project and document operations.

Mitigation: Store the API key in the agent environment or a secrets manager and avoid printing or committing it.

## Reference(s):

- [CellCog](https://cellcog.ai)
- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/project-management-cellcog)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with Python code blocks and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; produces instructions for remote project, document, context tree, and signed URL workflows.]

## Skill Version(s):

1.0.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
