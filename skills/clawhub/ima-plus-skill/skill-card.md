## Description:

IMA.plus skill for note management and knowledge-base operations, including natural-language path resolution, file upload and export, knowledge-base ZIP export, folder and item management, tags, permissions, public-square discovery, web links, and note search, browsing, creation, and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwqww1](https://clawhub.ai/user/wwqww1)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate IMA.plus notes and knowledge bases from an agent workflow, including creating or appending notes, uploading and exporting knowledge-base content, and managing folders, tags, permissions, and knowledge items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires reusable IMA OpenAPI credentials with broad note and knowledge-base access.

Mitigation: Provision credentials through official account or developer settings, keep them in environment variables, and do not ask an assistant to print secret values into chat.

Risk: The skill can perform write, export, permission, tag-delete, join, move, rename, and append operations over private content.

Mitigation: Confirm the target, content, and intended side effect before any append, move, rename, permission, tag-delete, join, or export operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwqww1/skills/ima-plus-skill)
- [IMA developer settings](https://ima.qq.com/agent-interface)
- [IMA service](https://ima.qq.com)
- [Knowledge-base API reference](knowledge-base/references/api.md)
- [Notes API reference](notes/references/api.md)
- [Troubleshooting reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run Node.js scripts that call IMA APIs and write exported knowledge-base files when the user confirms the target operation.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
