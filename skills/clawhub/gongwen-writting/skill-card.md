## Description:

秘书材料星公文写作-妙笔skill helps office, administrative, secretary, and materials-writing staff draft and revise Chinese official documents across 38 document types using template-guided Q&A, online writing knowledge retrieval, GB/T 9704 formatting guidance, and placeholder marking for missing facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yourtsao](https://clawhub.ai/user/yourtsao)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users in office, administrative, secretary, and materials-writing roles use this skill to turn document requirements, meeting notes, research material, or rough drafts into structured Chinese official documents and reports. The skill supports drafting, rewriting, polishing, shortening, expanding, title optimization, structure adjustment, tone alignment, content review, and GB/T 9704 Word-format guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends registration email, document request text, and payment or order data to a third-party gateway.

Mitigation: Use it only with material your organization permits sharing with that third-party service, and avoid confidential, regulated, or sensitive internal content unless approved.

Risk: The skill stores an account token locally in config.json.

Mitigation: Protect the skill directory and do not expose USER_TOKEN in conversations, logs, screenshots, or shared artifacts.

Risk: External API responses influence the generated document workflow.

Mitigation: Review generated drafts before use and verify facts, formatting, policy claims, dates, names, and numbers against source materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yourtsao/skills/gongwen-writting)
- [Publisher profile](https://clawhub.ai/user/yourtsao)
- [Word export guide](artifact/references/word-export.md)
- [Configured gateway](https://gongwen-api.xyz)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with optional Python snippets, shell setup commands, configuration updates, and docx formatting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require email registration, network access to the publisher gateway, quota tokens, and local config.json updates; missing facts are marked with 待补 placeholders.]

## Skill Version(s):

1.0.62 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
