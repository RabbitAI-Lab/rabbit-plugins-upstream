## Description:

IMA.plus Skill helps agents manage IMA notes and knowledge bases, including file upload and export, ZIP packaging, folders, tags, permissions, discovery, and note search, browsing, creation, and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwqww1](https://clawhub.ai/user/wwqww1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to automate IMA note and knowledge-base workflows through documented Node.js scripts and API calls. It is intended for managing private or team content with explicit user direction for export, mutation, permission, and delivery actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses powerful IMA API credentials that can access private notes and knowledge-base content.

Mitigation: Use a managed secret mechanism or fresh scoped credentials when available; do not paste API keys into unrelated chats or package any config.json containing credentials.

Risk: Export, signed download URL, permission, note edit, tag deletion, and ZIP delivery workflows can disclose or mutate private content.

Mitigation: Require explicit user intent and confirmation before running export, delivery, permission-changing, note-editing, tag-deleting, or bulk ZIP workflows.

Risk: The server security verdict marks the release suspicious because it asks users to expose credentials in chat and store them on disk while enabling broad export and mutation actions.

Mitigation: Review the skill carefully before installation, verify the credential-handling path, and restrict execution to the documented IMA and COS endpoints.

Risk: Incorrect text encoding during note writes can permanently garble user content.

Mitigation: Validate and normalize all title and content strings as legal UTF-8 before import_doc or append_doc calls, especially on PowerShell 5.1.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wwqww1/skills/ima-plus-skill)
- [Troubleshooting guide](references/troubleshooting.md)
- [IMA knowledge-base API reference](knowledge-base/references/api.md)
- [IMA notes API reference](notes/references/api.md)
- [IMA OpenAPI endpoint](https://ima.qq.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; some workflows produce local files such as exported ZIP archives.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer and user-provisioned IMA OpenAPI credentials.]

## Skill Version(s):

1.0.6 (source: server release metadata and artifact meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
