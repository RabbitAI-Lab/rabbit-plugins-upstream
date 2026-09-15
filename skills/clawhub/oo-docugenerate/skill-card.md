## Description:

DocuGenerate lets agents read, create, update, and delete DocuGenerate templates and generated documents through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate DocuGenerate from an agent, including generating documents from templates, listing and retrieving templates or documents, renaming documents, and deleting generated documents when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup asks users to run remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path before installing and prefer an official, versioned, verifiable installer when available.

Risk: update_document and delete_document can change or permanently remove DocuGenerate data.

Mitigation: Confirm the exact action, payload, and target document ID with the user before allowing write or destructive actions.

## Reference(s):

- [DocuGenerate homepage](https://www.docugenerate.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docugenerate)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON connector responses containing data and meta.executionId; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
