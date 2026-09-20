## Description:

Assists Chinese official-document drafting by guiding inputs, retrieving online templates and writing skeletons for 38 document types, and producing editable drafts with missing facts marked for completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yourtsao](https://clawhub.ai/user/yourtsao)

### License/Terms of Use:

MIT-0

## Use Case:

Office, administrative, secretarial, and materials-writing staff use this skill to draft, revise, structure, and format Chinese official documents such as requests, reports, meeting minutes, notices, speeches, summaries, plans, and formal correspondence. It is intended for agent-assisted drafting where the user supplies the topic, document type, key facts, and review context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafting requests and registration email may be sent to an external online service.

Mitigation: Use only for content the user is comfortable sending to that service; avoid private, sensitive, or non-official writing unless the user accepts that data flow.

Risk: Server responses can steer the agent workflow, including quota and payment prompts.

Mitigation: Review server-returned instructions before acting, require explicit user confirmation before registration or payment steps, and do not expose local tokens or credentials.

Risk: Generated official-document drafts may contain incomplete or user-supplied facts that need verification.

Mitigation: Keep missing facts marked for completion and require human review for names, dates, document numbers, policy citations, and final organizational wording before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yourtsao/skills/gongwen-writing)
- [Publisher profile](https://clawhub.ai/user/yourtsao)
- [Word export guide](artifact/references/word-export.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text, with optional code snippets and Word export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request an email for quota management, may call an external drafting service, and may direct users into a paid flow after free quota is used.]

## Skill Version(s):

1.0.70 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
