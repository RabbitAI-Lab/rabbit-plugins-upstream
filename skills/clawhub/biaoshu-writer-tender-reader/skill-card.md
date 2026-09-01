## Description:

Uploads tender and bid documents to the 百炼®标书 cloud service to interpret bid requirements, generate editable .docx bid files, review compliance risks, and compare 2-3 bid files for similarity or duplicate-risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to analyze tender files, produce draft bid documents, review bid submissions for compliance concerns, and check legally held bid files for similarity risks before submission. The skill requires a user-provided 百炼®标书 API key and explicit handling of local tender or bid files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercially sensitive, pricing, or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm user awareness and consent before first upload, and only process files the user explicitly provides as local uploads or paths.

Risk: The API key grants account access and is stored locally for the skill.

Mitigation: Have the user write the key directly to local configuration, do not request or echo it in chat, and remove or reset the key when access is no longer needed.

Risk: Bid generation may consume the account's available words, and submission can be blocked when available words are insufficient.

Mitigation: Check available words before submission and confirm deliberate generation steps before starting tasks that can affect the account balance.

Risk: Duplicate-risk checks could be mistaken for a legal conclusion about collusion or bid validity.

Mitigation: Require confirmation that the user legally holds and may process all uploaded files, and present duplicate results only as internal pre-submission risk signals.

## Reference(s):

- [百炼®标书 Open API contract](references/api.md)
- [Execution and usage guide](references/usage.md)
- [Knowledge-base field guide](references/knowledge-fields.md)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-tender-reader)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses with JSON results, HTML or Word reports, editable .docx bid documents, local configuration, and shell-command-backed workflow guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided API key; uploads local tender and bid files to 百炼®标书; generated bid documents may consume account available words.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
