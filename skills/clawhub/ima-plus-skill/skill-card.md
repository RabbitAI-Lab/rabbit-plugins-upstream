## Description:

Helps agents manage IMA knowledge bases and notes, including file imports and exports, tagging, permissions, note editing, and packaging local videos as HTML for upload.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwqww1](https://clawhub.ai/user/wwqww1)

### License/Terms of Use:

MIT-0

## Use Case:

IMA users and their agents use this skill to organize knowledge bases and notebooks, import and export content, edit notes, and upload local videos as HTML through the IMA API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs users to disclose existing IMA API credentials in chat.

Mitigation: Do not print credentials in chat; create or rotate your own scoped API key through the official IMA portal and configure it privately.

Risk: Note edits, tag changes, and knowledge-base permission changes can have irreversible or account-wide effects without enforced confirmation.

Mitigation: Review the target and requested change and obtain explicit user confirmation before account-changing or destructive operations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wwqww1/skills/ima-plus-skill)
- [IMA OpenAPI credential portal](https://ima.qq.com/agent-interface)
- [IMA API call templates](references/api-call-templates.md)
- [Knowledge-base API reference](knowledge-base/references/api.md)
- [Notes API reference](notes/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text and Markdown with shell commands and API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update IMA content and produce exported files or HTML-wrapped local videos.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
