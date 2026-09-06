## Description:

Upload, edit, and export documents via Nudocs.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to upload local documents to Nudocs for hosted editing, retrieve private edit links, list documents, export edited content, and delete specific remote documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded documents leave the local environment for Nudocs processing.

Mitigation: Disclose the data boundary before upload and require explicit action-time confirmation for sensitive documents.

Risk: Nudocs API keys and edit links can expose private documents if printed or shared.

Mitigation: Keep API keys in protected local or CI secret storage, never place secrets in chat or command arguments, and treat returned edit links as private unless the user approves a separate sharing action.

Risk: Deleting a remote document is destructive and recovery is not assumed.

Mitigation: Resolve the exact document ID, show the delete semantics, obtain immediate approval, execute once, and verify the target is gone.

## Reference(s):

- [Nudocs Skill Page](https://clawhub.ai/jdrhyne/skills/nudocs)
- [Nudocs CLI Source](https://github.com/PSPDFKit-labs/nudocs-cli)
- [Nudocs](https://nudocs.ai)
- [Nudocs CLI Formats](references/formats.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return private Nudocs edit links and exported document files through the installed CLI.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
