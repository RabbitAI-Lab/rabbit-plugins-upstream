## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩、润色、审校、文种核对、去口语化、降 AI 味及 Word 格式处理，适用于机关、企事业单位、学校和新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users in government agencies, companies, schools, and news organizations use the skill to draft, revise, condense, review, and format Chinese official, workplace, and news documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-generated or revised drafts may contain errors or omissions in facts, figures, citations, policy bases, responsibilities, or commitments.

Mitigation: Have a responsible reviewer verify these details before using a draft officially.

Risk: The skill can read files, while the host runtime determines which files it can access.

Mitigation: Limit access to files appropriate for the task and host permissions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [Project source and feedback](https://github.com/gongyu0918-debug/chinese-official-writing-skill)
- [Writing rules](artifact/references/writing-rules.md)
- [Review checklist](artifact/references/review-checklist.md)
- [Official document formatting guide](artifact/references/format-gbt9704.md)
- [AI computing documents guide](artifact/references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Chinese prose, review comments, and structured document drafts; Word files when host document tools are available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts and edits are based on supplied materials; verify facts, figures, citations, policies, responsibilities, and commitments before official use.]

## Skill Version(s):

2.0.56 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
